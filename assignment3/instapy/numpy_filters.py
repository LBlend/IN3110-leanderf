"""numpy implementation of image filters"""

from typing import Optional
import numpy as np


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.empty_like(image)
    gray_image = np.dot(image, [0.21, 0.72, 0.07])

    return gray_image


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_matrix = np.array([
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ])

    #sepia_image = np.average(image, weights=sepia_matrix, axis=(1, 1))

    sepia_image = np.dot(image, sepia_matrix.T)
    sepia_image /= sepia_image.max()  # Scale down to 0-1
    sepia_image *= 255  # Scale up to rgb range
    sepia_image = sepia_image.astype(np.uint8)

    # Return image (make sure it's the right type!)
    return sepia_image


if __name__ == '__main__':
    from instapy import io
    image = io.read_image(filename='assignment3/test_image.jpg')
    gray_image = numpy_color2gray(image)
    io.display(gray_image)

    sepia_image = numpy_color2sepia(image)
    io.display(sepia_image)
