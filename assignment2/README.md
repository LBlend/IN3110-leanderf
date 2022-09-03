# Array

## Usage

### Creating a 1-dimensional array

```python
array = Array((4,), 1, 2, 3, 4)
print(array)  # [1, 2, 3, 4]
```

### Creating a 2-dimensional array

```python
array = Array((3, 2), 1, 2, 3, 4, 5, 6)
print(array)  # [[1, 2], [3, 4], [5, 6]]
```

See unit tests for further usage. (I'm too lazy to document this crap)

## Testing

To run the unit tests, simply run the following command from the [assignment2](assignment2) directory.

```
pytest
```

**Note that you'll need to install `pytest` in order to these tests**

If you want to see the test coverage, you can run the following command

```
coverage run --module pytest --verbose && coverage report --show-missing
```

**In order for this to work, you'll need to install `pytest-cov` as well.**
