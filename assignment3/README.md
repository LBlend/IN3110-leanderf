# instapy

A package that turns your images into nostalgic memories.

Allows you to turn any image into a sepia or black and white version of itself. Can be used as a library or as a CLI application.

## Installation

1. Clone the repo
2. Make sure that your current working directory is the one that this README is located in.
3. Install the package with pip

_Assuming that your PATH is pointed to a Python 3.7 installation pip._

```
pip install .
```

## Usage

### CLI

instapy includes a command line interface! For usage info, run the following command:

```
python -m instapy --help
```

### Package

Here's a typical usage example. Converting an image to grayscale, saving it and then displaying it.

```python
from instapy.io import read_image, write_image, display
from instapy.numpy_filters import color2gray

image = read_image("my_epic_image.jpg")
grayscale = color2gray(image)
write_image(grayscale, "my_new_epic_image.jpg")
display(grayscale)
```
