"""
Tests for our array class
"""

from array_class import Array
import pytest

# 1D tests (Task 4)


def test_str_1d():
    array = Array((4,), 1, 2, 3, 4)
    assert str(array) == "[1, 2, 3, 4]"


def test_add_1d():
    # Add 1 to array of ints
    array = Array((4,), 1, 2, 3, 4)
    array = array + 1
    assert array == Array((4,), 2, 3, 4, 5)

    # Add 1 to array of floats
    array = Array((4,), 1.1, 2.2, 3.3, 4.4)
    array = array + 1
    assert array == Array((4,), 2.1, 3.2, 4.3, 5.4)

    # Add 1.1 to array of floats
    array = Array((4,), 1.0, 2.0, 3.0, 4.0)
    array = array + 1.1
    assert array == Array((4,), 2.1, 3.1, 4.1, 5.1)

    # Add array of floats to 2
    array = Array((4,), 1.0, 2.0, 3.0, 4.0)
    array = 2 + array
    assert array == Array((4,), 3.0, 4.0, 5.0, 6.0)

    # Add array with another array
    array = Array((4,), 1.0, 2.0, 3.0, 4.0)
    array = array + Array((4,), 5, 2, 4, 10)
    assert array == Array((4,), 6, 4, 7, 14)

    # Test for exceptions
    with pytest.raises(ValueError):
        array = Array((4,), 1.0, 2.0, 3.0, 4.0)
        array = array + Array((5,), 5, 2, 4, 10, 11)
    with pytest.raises(NotImplementedError):
        array = Array((4,), 1.0, 2.0, 3.0, 4.0)
        array = array + "yeet"


def test_sub_1d():
    # Subtract 1 to array of ints
    array = Array((4,), 1, 2, 3, 4)
    array = array - 1
    assert array == Array((4,), 0, 1, 2, 3)

    # Subtract 1 to array of floats
    array = Array((1,), 1.8)
    array = array - 1
    assert array == Array((1,), 0.8)

    # Subtract 1.1 to array of floats
    array = Array((1,), 8.1)
    array = array - 1.1
    assert array == Array((1,), 7.0)

    # Subtract array of floats to 2
    array = Array((1,), 4.0)
    array = 2 - array
    assert array == Array((1,), -2.0)

    # Subtract array with another array
    array = Array((4,), 1.0, 2.0, 3.0, 4.0)
    array = array - Array((4,), 5, 2, 4, 10)
    assert array == Array((4,), -4, 0, -1, -6)

    # Test for exceptions
    with pytest.raises(ValueError):
        array = Array((4,), 1.0, 2.0, 3.0, 4.0)
        array = array - Array((5,), 5, 2, 4, 10, 11)
    with pytest.raises(NotImplementedError):
        array = Array((4,), 1.0, 2.0, 3.0, 4.0)
        array = array - "yeet"


def test_mul_1d():
    # Multiply 2 to array of ints
    array = Array((4,), 1, 2, 3, 4)
    array = array * 2
    assert array == Array((4,), 2, 4, 6, 8)

    # Multiply 2 to array of floats
    array = Array((1,), 2.2)
    array = array * 2
    assert array == Array((1,), 4.4)

    # Multiply 1.1 to array of floats
    array = Array((3,), 1.0, 2.0, 4.0)
    array = array * 1.1
    assert array == Array((3,), 1.1, 2.2, 4.4)

    # Multiply array of floats to 2
    array = Array((4,), 1.0, 2.0, 3.0, 4.0)
    array = 2 * array
    assert array == Array((4,), 2.0, 4.0, 6.0, 8.0)

    # Multiply array with another array
    array = Array((4,), 1.0, 2.0, 3.0, 4.0)
    array = array * Array((4,), 5, 2, 4, 10)
    assert array == Array((4,), 5, 4, 12, 40)

    # Test for exceptions
    with pytest.raises(ValueError):
        array = Array((4,), 1.0, 2.0, 3.0, 4.0)
        array = array * Array((5,), 5, 2, 4, 10, 11)
    with pytest.raises(NotImplementedError):
        array = Array((4,), 1.0, 2.0, 3.0, 4.0)
        array = array * "yeet"


def test_eq_1d():
    array = Array((4,), 1, 2, 3, 4)
    array2 = Array((4,), 1, 2, 3, 4)
    is_equal = array == array2
    assert is_equal is True

    array = Array((4,), 1, 2, 3, 4)
    array2 = Array((4,), 1, 2, 3, 5)
    is_equal = array == array2
    assert is_equal is False

    array = Array((4,), 1, 2, 3, 4)
    array2 = Array((2,), 1, 2)
    is_equal = array == array2
    assert is_equal is False

    array = Array((4,), 1, 2, 3, 4)
    is_equal = array == "yeet"
    assert is_equal is False


def test_same_1d():
    array = Array((4,), 1, 2, 3, 4)
    array2 = Array((4,), 1, 2, 3, 4)
    assert array.is_equal(array2) == Array((4,), 1, 1, 1, 1)

    array = Array((4,), 1, 2, 3, 4)
    array2 = Array((4,), 1, 2, 42, 4)
    assert array.is_equal(array2) == Array((4,), 1, 1, 0, 1)
    assert array.is_equal(array2) == Array((4,), True, True, False, True)

    assert array.is_equal(1) == Array((4,), 1, 0, 0, 0)

    # Test for exceptions
    with pytest.raises(ValueError):
        array2 = Array((5,), 1, 2, 42, 4, 10)
        array.is_equal(array2)
    with pytest.raises(TypeError):
        array.is_equal([1, 2, 42, 4])


def test_smallest_1d():
    array = Array((4,), 1, 2, 3, 4)
    assert array.min_element() == 1

    array = Array((5,), 4, 6, -2, 3, -1)
    assert array.min_element() == -2

    # Test for exceptions
    with pytest.raises(TypeError):
        array = Array((4,), True, False, True, False)
        array.min_element()


def test_mean_1d():
    array = Array((4,), 1, 2, 3, 4)
    assert array.mean_element() == 2.5

    # Test for exceptions
    with pytest.raises(TypeError):
        array = Array((4,), True, False, True, False)
        array.mean_element()


# 2D tests (Task 6)


def test_add_2d():
    # Add 1 to array of ints
    array = Array((2, 2), 1, 2, 3, 4)
    array = array + 1
    assert array == Array((2, 2), 2, 3, 4, 5)

    # Add 1 to array of floats
    array = Array((2, 2), 1.1, 2.2, 3.3, 4.4)
    array = array + 1
    assert array == Array((2, 2), 2.1, 3.2, 4.3, 5.4)

    # Add 1.1 to array of floats
    array = Array((2, 2), 1.0, 2.0, 3.0, 4.0)
    array = array + 1.1
    assert array == Array((2, 2), 2.1, 3.1, 4.1, 5.1)

    # Add array of floats to 2
    array = Array((2, 2), 1.0, 2.0, 3.0, 4.0)
    array = 2 + array
    assert array == Array((2, 2), 3.0, 4.0, 5.0, 6.0)

    # Add array with another array
    array = Array((2, 2), 1.0, 2.0, 3.0, 4.0)
    array = array + Array((2, 2), 5, 2, 4, 10)
    assert array == Array((2, 2), 6, 4, 7, 14)


def test_mult_2d():
    # Multiply 2 to array of ints
    array = Array((2, 2), 1, 2, 3, 4)
    array = array * 2
    assert array == Array((2, 2), 2, 4, 6, 8)

    # Multiply 2 to array of floats
    array = Array((2, 1), 2.2, 2.2)
    array = array * 2
    assert array == Array((2, 1), 4.4, 4.4)

    # Multiply 1.1 to array of floats
    array = Array((3, 1), 1.0, 2.0, 4.0)
    array = array * 1.1
    assert array == Array((3, 1), 1.1, 2.2, 4.4)

    # Multiply array of floats to 2
    array = Array((2, 2), 1.0, 2.0, 3.0, 4.0)
    array = 2 * array
    assert array == Array((2, 2), 2.0, 4.0, 6.0, 8.0)

    # Multiply array with another array
    array = Array((2, 2), 1.0, 2.0, 3.0, 4.0)
    array = array * Array((2, 2), 5, 2, 4, 10)
    assert array == Array((2, 2), 5, 4, 12, 40)


def test_same_2d():
    array = Array((2, 2), 1, 2, 3, 4)
    array2 = Array((2, 2), 1, 2, 3, 4)
    assert array.is_equal(array2) == Array((2, 2), 1, 1, 1, 1)

    array = Array((2, 2), 1, 2, 3, 4)
    array2 = Array((2, 2), 1, 2, 42, 4)
    assert array.is_equal(array2) == Array((2, 2), 1, 1, 0, 1)
    assert array.is_equal(array2) == Array((2, 2), True, True, False, True)


def test_mean_2d():
    array = Array((2, 2), 1, 2, 3, 4)
    assert array.mean_element() == 2.5


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
