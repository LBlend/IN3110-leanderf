from instapy.python_filters import python_color2gray, python_color2sepia


def test_color2gray(image):
    # run color2gray
    grayscale = python_color2gray(image)
    
    # check that the result has the right shape, type
    assert grayscale.shape == image.shape
    assert grayscale.dtype == image.dtype

    # assert uniform r,g,b values
    # checking top left 5x5 pixels
    for i in range(5):
        for j in range(5):
            assert grayscale[i][j][0] == grayscale[i][j][1] == grayscale[i][j][2]

def test_color2sepia(image):
    # run color2sepia
    sepia = python_color2sepia(image)

    # check that the result has the right shape, type
    assert sepia.shape == image.shape
    assert sepia.dtype == image.dtype

    # verify some individual pixel samples
    # according to the sepia matrix
