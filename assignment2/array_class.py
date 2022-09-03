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
                raise TypeError("Values needs to be a numbered type")
        except IndexError:
            pass
        else:
            for value in values:
                if not isinstance(value, type(values[0])):
                    raise ValueError("The array can only hold one datatype")

        # Check that the amount of values corresponds to the shape
        if len(values) != shape[0]:
            raise ValueError("The number of values given must match the given shape.")

        # Set class-variables
        self.shape = shape
        self.values = list(values)

    def __getitem__(self, index):
        """Returns the value stored at the given index in the array

        Args:
            index:
                int: The index you want to fetch the value from.

        Returns:
            index (int): Value stored at index.

        """

        return self.values[index]

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        return ", ".join(str(value) for value in self.values)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """

        # check that the method supports the given arguments (check for data type and shape of array)
        # if the array is a boolean you should return NotImplemented
        if isinstance(other, (int, float)):
            new_array = list(map(lambda x: x + other, self.values))
        elif isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("The shape must match the existing array's shape")
            # Do I need to check the types within the collection?
            new_array = list(map(lambda x, y: x + y, zip(self.values, other)))
        else:
            raise NotImplemented()

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

        """
        if isinstance(other, (int, float)):
            new_array = list(map(lambda x: x - other, self.values))
        elif isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("The shape must match the existing array's shape")
            # Do I need to check the types within the collection?
            new_array = list(map(lambda x, y: x - y, zip(self.values, other)))
        else:
            raise NotImplemented()

        return Array(self.shape, *new_array)

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        if isinstance(other, (int, float)):
            new_array = list(map(lambda x: other - x, self.values))
        elif isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("The shape must match the existing array's shape")
            # Do I need to check the types within the collection?
            new_array = list(map(lambda x, y: y - x, zip(self.values, other)))
        else:
            raise NotImplemented()

        return Array(self.shape, *new_array)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        if isinstance(other, (int, float)):
            new_array = list(map(lambda x: x * other, self.values))
        elif isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("The shape must match the existing array's shape")
            # Do I need to check the types within the collection?
            new_array = list(map(lambda x, y: x * y, zip(self.values, other)))
        else:
            raise NotImplemented()

        return Array(self.shape, *new_array)

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

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
            for x, y in zip(self.values, other):
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

        """
        if isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("The shape must match the existing array's shape")
            new_array = list(map(lambda x, y: x == y, zip(self.values, other)))
        elif isinstance(other, (int, float)):
            new_array = list(map(lambda x: x == other), self.values)
        else:
            raise TypeError("You can only compare another array or a number with the current array")

        return Array(self.shape, *new_array)

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """
        try:
            if isinstance(self.values[0], bool):
                raise TypeError("Does not work for boolean arrays")
        except IndexError:
            raise IndexError("Array cannot empty")

        # return min(self.values)
        smallest = float("inf")
        for value in self.values:
            if value < smallest:
                smallest = value

        return smallest

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """
        try:
            if isinstance(self.values[0], bool):
                raise TypeError("Does not work for boolean arrays")
        except IndexError:
            raise IndexError("Array cannot be empty")

        #return mean(self.values)
        #return sum(self.values) / len(self.values)
        total = 0
        for value in self.values:
            total += value
        
        return total / len(self.values)
