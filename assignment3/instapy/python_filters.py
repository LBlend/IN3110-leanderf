"""pure Python implementation of image filters"""

import numpy as np


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    DOES NOT SUPPORT ALPHA CHANNELS

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform

    for row in range(image.shape[0]):  # height
        for col in range(image.shape[1]):  # width
            red, green, blue = image[row][col]
            weighted_sum = red*0.21 + green*0.72 + blue*0.07
            gray_image[row][col] = [weighted_sum, weighted_sum, weighted_sum]

    return gray_image


def python_color2sepia(image: np.array) -> np.array:
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
    gray_image = python_color2gray(image)
    io.display(gray_image)
