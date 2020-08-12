# `autogoal.utils.compute_class_weights`

> [📝](https://github.com/autogoal/autogoal/blob/main/autogoal/utils/__init__.py#L144)
> `compute_class_weights(y)`

Computes relative class weights for imbalanced datasets. Works with nested input.

##### Examples

```python
>>> compute_class_weights([['A', 'B', 'A'], ['C'], ['C', 'C']])
{'A': 1.5, 'B': 3.0, 'C': 1.0}

```
