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


@jit(nopython=True)
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)

    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]
    
    for row in range(image.shape[0]):  # height
        for col in range(image.shape[1]):  # width
            red, green, blue = image[row][col]
            avg_weighted_red = min(255, (red * sepia_matrix[0][0] + green * sepia_matrix[0][1] + blue * sepia_matrix[0][2]) / 3)
            avg_weighted_green = min(255, (red * sepia_matrix[1][0] + green * sepia_matrix[1][1] + blue * sepia_matrix[1][2]) / 3)
            avg_weighted_blue = min(255, (red * sepia_matrix[2][0] + green * sepia_matrix[2][1] + blue * sepia_matrix[2][2]) / 3)
            sepia_image[row][col] = [avg_weighted_red, avg_weighted_green, avg_weighted_blue]

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

    sepia_image = numba_color2sepia(image)
    io.display(sepia_image)

    # Test 2 images because of numba's inherent cold start compilation
    sepia_image2 = numba_color2sepia(image2)
    io.display(sepia_image2)
