# `autogoal.utils`

## Classes

### `ResourceManager`

> [📝](https://github.com/sestevez/autogoal/blob/master/autogoal/utils/_resource.py#L9)
> `ResourceManager(self, time_limit=300, memory_limit=4294967296)`


Resource manager class.

##### Parameters

- `time_limit: int`: maximum amount of seconds a function can run for (default = `5 minutes`).
- `ram_limit: int`: maximum amount of memory bytes a function can use (default = `4 GB`).

##### Notes

- Only one function may be restricted at the same time.
  Upcoming updates will fix this matter.
- Memory restriction is issued upon the process's heap memory size and not
  over total address space in order to get a better estimation of the used memory.



## Functions

### `nice_repr`

> [📝](https://github.com/sestevez/autogoal/blob/master/autogoal/utils/__init__.py#L6)
> `nice_repr(cls)`


!!! warning
    This class has no docstrings.

