from instapy.numba_filters import numba_color2gray, numba_color2sepia

import numpy.testing as nt


def test_color2gray(image, reference_gray):
    # run color2gray
    grayscale = numba_color2gray(image)
    nt.assert_allclose(grayscale, reference_gray)


def test_color2sepia(image, reference_sepia):
    # run color2sepia
    sepia = numba_color2sepia(image)
    nt.assert_allclose(sepia, reference_sepia)
