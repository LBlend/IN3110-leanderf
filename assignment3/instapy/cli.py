"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from __init__ import get_filter
from instapy.io import display, write_image


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    
    # load the image from a file
    image = Image.open(file)
    if scale != 1:
        image = image.resize((image.width // 2, image.height // 2))
    
    image = np.asarray(image)  # Convert to numpy array

    # Apply the filter
    filter_function = get_filter(filter=filter, implementation=implementation)
    filtered = filter_function(image)
    
    if out_file:
        write_image(filtered, out_file)
    else:
        # not asked to save, display it instead
        display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Add required arguments
    ...

    # parse arguments and call run_filter
    ...
