# `autogoal.ml.AutoML`

> [📝](https://github.com/autogal/autogoal/blob/master/autogoal/ml/__init__.py#L23)
> `AutoML(self, input=None, output=None, random_state=None, search_algorithm=<class 'autogoal.search._pge.PESearch'>, search_kwargs={}, search_iterations=100, include_filter='.*', exclude_filter=None, validation_split=0.3, errors='warn', cross_validation='median', cross_validation_steps=3, registry=None, score_metric=None)`

Predefined pipeline search with automatic type inference.

An `AutoML` instance represents a general-purpose machine learning
algorithm, that can be applied to any input and output.
### `fit`

> [📝](https://github.com/autogoal/autogoal/blob/master/autogoal/ml/__init__.py#L76)
> `fit(self, X, y, **kwargs)`

### `fit_pipeline`

> [📝](https://github.com/autogoal/autogoal/blob/master/autogoal/ml/__init__.py#L94)
> `fit_pipeline(self, X, y)`

### `load_pipeline`

> [📝](https://github.com/autogoal/autogoal/blob/master/autogoal/ml/__init__.py#L113)
> `load_pipeline(self, fp)`

Loads the state of the best pipeline and retrains.
You are responsible for opening and closing the stream.

After calling load, the best pipeline is **not** trained.
You need to retrain it by calling `fit_pipeline(X, y)`.
### `predict`

> [📝](https://github.com/autogoal/autogoal/blob/master/autogoal/ml/__init__.py#L168)
> `predict(self, X)`

### `save_pipeline`

> [📝](https://github.com/autogoal/autogoal/blob/master/autogoal/ml/__init__.py#L102)
> `save_pipeline(self, fp)`

Saves the state of the best pipeline.
You are responsible for opening and closing the stream.
### `score`

> [📝](https://github.com/autogoal/autogoal/blob/master/autogoal/ml/__init__.py#L125)
> `score(self, X, y)`

