"""numba-optimized filters"""
from numba import jit
import numpy as np

@jit(nopython=True)
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    
    for row in range(image.shape[0]):  # height
        for col in range(image.shape[1]):  # width
            red, green, blue = image[row][col]
            weighted_sum = red*0.21 + green*0.72 + blue*0.07
            gray_image[row][col] = [weighted_sum, weighted_sum, weighted_sum]

    return gray_image


def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix

    ...

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image


if __name__ == '__main__':
    from instapy import io
    image = io.read_image(filename='assignment3/test_image.jpg')
    gray_image = numba_color2gray(image)
    io.display(gray_image)

    # Test 2 images because of numba's inherent cold start compilation
    image2 = io.read_image(filename='assignment3/test_image2.jpg')
    gray_image2 = numba_color2gray(image2)
    io.display(gray_image2)
