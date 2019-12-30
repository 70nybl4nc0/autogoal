# coding: utf8

import networkx as nx
import random

from typing import List


class Graph(nx.DiGraph):
    def __init__(self, **attrs):
        super(Graph, self).__init__(**attrs)

    def build_order(self):
        """
        Returns a iterable of `(node, in_nodes)` in topological order.

        In detail, returns every `node` and the list of nodes that are incoming edges to `node`.
        This way, you can call a method on each node whose args are the
        previous nodes.
        """
        for node in nx.topological_sort(self):
            in_nodes = [u for u,v in self.in_edges(node)]
            yield (node, in_nodes)

    def apply(self, function):
        """
        Applies a function to all nodes in `build_order`'s order.

        The function receives the current three arguments:
            - The current `node` instance
            - A list of incoming node instances
            - A list of the result of the application of the
              function in the previous node instances.

        Returns the last of the values computed.
        """
        previous_values = {}

        for node, in_nodes in self.build_order():
            in_values = [previous_values[n] for n in in_nodes]
            value = function(node, in_nodes, in_values)
            previous_values[node] = value

        return value


def uniform_pattern_selection(patterns):
    return random.choice(patterns)


def default_init_factory(cls):
    return dict()


class Production:
    def __init__(self, pattern, replacement, *, init_factory=None):
        if not isinstance(pattern, Graph):
            obj = pattern
            pattern = Graph()
            pattern.add_node(obj)

        if not isinstance(replacement, GraphPattern):
            replacement = Node(replacement)

        self.pattern = pattern
        self.replacement = replacement
        self.init_factory = init_factory or default_init_factory

    def _matches(self, graph: Graph):
        # TODO: Generalizar a permitir cualquier tipo de grafo como patrón, no solo un nodo
        pattern_node = list(self.pattern.nodes)[0]

        for node in graph.nodes:
            if node.__class__ == pattern_node:
                yield node

    def match(self, graph: Graph):
        """
        Returns True if it finds a subgraph in `graph` that matches the pattern.
        NOTE: Right now only works if pattern is a single node.
        """
        for _ in self._matches(graph):
            return True

        return False

    def apply(
        self, graph: Graph, pattern_selection=uniform_pattern_selection
    ) -> Graph:
        """
        Applies a production in a graph and returns the modified graph.
        """
        matches = list(self._matches(graph))
        node = pattern_selection(matches)

        in_edges = graph.in_edges(node)
        out_edges = graph.out_edges(node)

        in_nodes = [u for u, v in in_edges]
        out_nodes = [v for u, v in out_edges]

        graph.remove_node(node)
        self.replacement.build(
            graph, in_nodes, out_nodes, init_factory=self.init_factory
        )

        return graph


def uniform_production_selector(productions: List[Production]) -> Production:
    return random.choice(productions)


class GraphPattern:
    def build(self, graph: Graph, in_nodes, out_nodes):
        raise NotImplementedError()

    def _add_in_nodes(self, graph, in_nodes, node):
        for in_node in in_nodes:
            graph.add_edge(in_node, node)

    def _add_out_nodes(self, graph, out_nodes, node):
        for out_node in out_nodes:
            graph.add_edge(node, out_node)

    def make(self, *, init_factory=default_init_factory) -> Graph:
        graph = Graph()
        self.build(graph, [], [], init_factory)
        return graph


class Node(GraphPattern):
    def __init__(self, cls):
        self.cls = cls

    def build(self, graph: Graph, in_nodes, out_nodes, init_factory):
        obj = self.cls(**init_factory(self.cls))
        graph.add_node(obj)
        self._add_in_nodes(graph, in_nodes, obj)
        self._add_out_nodes(graph, out_nodes, obj)


class Path(GraphPattern):
    def __init__(self, *items):
        self.items = list(items)

    def build(self, graph: Graph, in_nodes, out_nodes, init_factory):
        items = [cls(**init_factory(cls)) for cls in self.items]
        graph.add_nodes_from(items)

        for i, j in zip(items, items[1:]):
            graph.add_edge(i, j)

        self._add_in_nodes(graph, in_nodes, items[0])
        self._add_out_nodes(graph, out_nodes, items[-1])


class Block(GraphPattern):
    def __init__(self, *items):
        self.items = list(items)

    def build(self, graph: Graph, in_nodes, out_nodes, init_factory):
        items = [cls(**init_factory(cls)) for cls in self.items]
        graph.add_nodes_from(items)

        for item in items:
            self._add_in_nodes(graph, in_nodes, item)
            self._add_out_nodes(graph, out_nodes, item)


class GraphGrammar:
    def __init__(self):
        self.productions: List[Production] = []

    def add(self, pattern, replacement: GraphPattern, *, init_factory=None):
        self.productions.append(
            Production(pattern, replacement, init_factory=init_factory)
        )

    def expand(
        self, graph: Graph, max_iters=100, production_selector=uniform_production_selector,
    ) -> Graph:
        if graph is None:
            raise ValueError("`graph` cannot be `None`")

        if not isinstance(graph, Graph):
            obj = graph
            graph = Graph()
            graph.add_node(obj)
        else:
            graph = graph.copy()

        return self._expand(graph, max_iters, production_selector)

    def _expand(self, graph, iters, production_selector):
        if graph is None:
            raise ValueError("`graph` cannot be `None`")

        if iters == 0:
            return graph

        valid_productions = [p for p in self.productions if p.match(graph)]

        if not valid_productions:
            return graph

        production = production_selector(valid_productions)
        graph = production.apply(graph)

        return self._expand(graph, iters - 1, production_selector)
