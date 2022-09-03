"""
Array class for assignment 2
"""


class Array:
    def __init__(self, shape, *values):
        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.

        """

        # Check types
        if not isinstance(shape, tuple):
            raise TypeError("Shape needs to be a tuple")

        for value in shape:
            if not isinstance(value, int):
                raise TypeError("Shape needs to consist of only integer types")

        try:
            if not isinstance(values[0], (int, float, bool)):
                raise TypeError("Values needs to be a numbered or a boolean type")
        except IndexError:
            pass
        else:
            for value in values:
                if not isinstance(value, type(values[0])):
                    raise ValueError("The array can only hold one datatype")

        # Check that the amount of values corresponds to the shape
        product = 1
        for number_of_items in shape:
            product *= number_of_items
        if len(values) != product:
            raise ValueError("The number of values given must match the given shape.")

        # Set class-variables
        self.__flattened_values = list(values)
        self.shape = shape
        if len(shape) == 1:
            self.__values = self.__flattened_values
        else:
            self.__values = []
            number_of_items = 0
            for _ in range(self.shape[0]):
                end_index = number_of_items + self.shape[1]
                self.__values.append(self.__flattened_values[number_of_items:end_index])
                number_of_items += self.shape[1]

    def __getitem__(self, index):
        """Returns the value stored at the given index in the array

        Args:
            index:
                int: The index you want to fetch the value from.

        Returns:
            index (int): Value stored at index.

        """

        return self.__values[index]

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """

        return str(self.__values)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        Raises:
            ValueError: If the shape of the given array does not match the instance's one
            NotImplementedError If a value that is not an int, float or Array is passed to the funciton.

        """

        # check that the method supports the given arguments (check for data type and shape of array)
        # if the array is a boolean you should return NotImplemented
        if isinstance(other, (int, float)):
            new_array = list(map(lambda x: x + other, self.__flattened_values))
        elif isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("The shape must match the existing array's shape")
            # Do I need to check the types within the collection?
            new_array = list(map(lambda x: x[0] + x[1], zip(self.__flattened_values, other.__flattened_values)))
        else:
            raise NotImplementedError()

        return Array(self.shape, *new_array)

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """

        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        Raises:
            ValueError: If the shape of the given array does not match the instance's one
            NotImplementedError If a value that is not an int, float or Array is passed to the funciton.

        """

        if isinstance(other, (int, float)):
            new_array = list(map(lambda x: x - other, self.__flattened_values))
        elif isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("The shape must match the existing array's shape")
            # Do I need to check the types within the collection?
            new_array = list(map(lambda x: x[0] - x[1], zip(self.__flattened_values, other.__flattened_values)))
        else:
            raise NotImplementedError()

        return Array(self.shape, *new_array)

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        Raises:
            ValueError: If the shape of the given array does not match the instance's one
            NotImplementedError If a value that is not an int, float or Array is passed to the funciton.

        """

        if isinstance(other, (int, float)):
            new_array = list(map(lambda x: other - x, self.__flattened_values))
        elif isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("The shape must match the existing array's shape")
            # Do I need to check the types within the collection?
            new_array = list(map(lambda x: x[1] - x[0], zip(self.__flattened_values, other.__flattened_values)))
        else:
            raise NotImplementedError()

        return Array(self.shape, *new_array)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        Raises:
            ValueError: If the shape of the given array does not match the instance's one
            NotImplementedError If a value that is not an int, float or Array is passed to the funciton.

        """

        if isinstance(other, (int, float)):
            new_array = list(map(lambda x: x * other, self.__flattened_values))
        elif isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("The shape must match the existing array's shape")
            # Do I need to check the types within the collection?
            new_array = list(map(lambda x: x[0] * x[1], zip(self.__flattened_values, other.__flattened_values)))
        else:
            raise NotImplementedError()

        return Array(self.shape, *new_array)

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        Raises:
            ValueError: If the shape of the given array does not match the instance's one
            NotImplementedError If a value that is not an int, float or Array is passed to the funciton.

        """

        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """

        if isinstance(other, Array):
            if other.shape != self.shape:
                return False
            for x, y in zip(self.__values, other):
                if x != y:
                    return False
            return True

        return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.
            TypeError: if the type passed in is not an int, float or Array.

        """

        if isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("The shape must match the existing array's shape")
            new_array = list(map(lambda x: x[0] == x[1], zip(self.__flattened_values, other.__flattened_values)))
        elif isinstance(other, (int, float)):
            new_array = list(map(lambda x: x == other), self.__flattened_values)
        else:
            raise TypeError("You can only compare another array or a number with the current array")

        return Array(self.shape, *new_array)

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        Raises:
            IndexError: if the array is empty
            TypeError: if the method is called from a boolean array

        """

        try:
            if isinstance(self.__flattened_values[0], bool):
                raise TypeError("Does not work for boolean arrays")
        except IndexError:
            raise IndexError("Array cannot empty")

        # return min(self.__values)
        smallest = float("inf")
        for value in self.__flattened_values:
            if value < smallest:
                smallest = value

        return smallest

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value

        Raises:
            IndexError: if the array is empty
            TypeError: if the method is called from a boolean array

        """

        try:
            if isinstance(self.__values[0], bool):
                raise TypeError("Does not work for boolean arrays")
        except IndexError:
            raise IndexError("Array cannot be empty")

        # return mean(self.__values)
        # return sum(self.__values) / len(self.__values)
        total = 0
        for value in self.__flattened_values:
            total += value

        return total / len(self.__flattened_values)
