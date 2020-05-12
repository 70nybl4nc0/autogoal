# `autogoal.kb.infer_type`

> [📝](/usr/lib/python3/dist-packages/autogoal/kb/_data.py#L303)
> `infer_type(obj)`

Attempts to automatically infer the most precise semantic type for `obj`.

##### Parameters

* `obj`: Object to detect its semantic type.

##### Raises

* `TypeError`: if no valid semantic type was found that matched `obj`.

##### Examples

* Natural language

```python
>>> infer_type("hello")
Word()
>>> infer_type("hello world")
Sentence()
>>> infer_type("Hello Word. It is raining.")
Document()

```

* Vectors

```
>>> import numpy as np
>>> infer_type(np.asarray(["A", "B", "C", "D"]))
CategoricalVector()
>>> infer_type(np.asarray([0.0, 1.1, 2.1, 0.2]))
ContinuousVector()
>>> infer_type(np.asarray([0, 1, 1, 0]))
DiscreteVector()

```

* Matrices

```
>>> import numpy as np
>>> infer_type(np.random.randn(10,10))
MatrixContinuousDense()

>>> import scipy.sparse as sp
>>> infer_type(sp.coo_matrix((10,10)))
MatrixContinuousSparse()

```
