"""input/output utilities

for reading, writing, and displaying image files
as numpy arrays
"""

import numpy as np
from PIL import Image


def read_image(filename: str) -> np.array:
    """Read an image file to an rgb array
    
    Args:
        filename (str): The filename to read to array

    Returns:
        np.array: The image as an array
    """
    return np.asarray(Image.open(filename))


def write_image(array: np.array, filename: str) -> None:
    """Write a numpy pixel array to a file
    
    Args:
        array (np.array): The array to write from
        filename (str): The filename to write to
    """
    return Image.fromarray(array).save(filename)


def random_image(width: int = 320, height: int = 180) -> np.array:
    """Create a random image array of a given size
    
    Args:
        width (int, optional): The width of the image. Defaults to 320.
        height (int, optional): The height of the image. Defaults to 180.

    Returns:
        np.array: The random image
    """
    return np.random.randint(0, 255, size=(height, width, 3), dtype=np.uint8)


def display(array: np.array):
    """Show an image array on the screen
    
    Parameters
    ----------
    array : np.array
        The array to display
    """
    Image.fromarray(array).show()
