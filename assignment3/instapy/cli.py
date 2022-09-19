"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

from instapy import get_filter
from instapy.io import display, read_image, write_image
from instapy.timing import time_one


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter
    
    Args:
        file (str): The file to apply filter to
        out_file (str: The output filename. by default None
        implementation (str): The implementation, by default "python"
        filter (str): The filter to apply, by default "color2gray"
        scale (int): The scale factor to resize the image, by default 1
    """
    
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
    """Parse the command-line and call run_filter with the arguments
    
    Args:
        argv (list, optional): The command-line arguments. Defaults to None.
    """
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", type=str,
                        help="The filename to apply filter to")

    parser.add_argument('-o', '--out', type=str,
                        help='The output filename')
    
    filter_group = parser.add_mutually_exclusive_group(required=True)
    filter_group.add_argument('-g', '--gray', action='store_const', const='color2gray',
                        help='Select gray filter')
    filter_group.add_argument('-se', '--sepia', action='store_const', const='color2sepia',
                        help='Select sepia filter')

    parser.add_argument('-sc', '--scale', type=int, nargs=1, default=1,
                        help='Scale factor to resize image')
    parser.add_argument('-i', '--implementation', choices=['python', 'numba', 'numpy'], default='numpy',
                        help='The implementation')
    parser.add_argument('-r', '--runtime', default='numpy', action='store_true',
                        help='Time the average runtime of the filter (3 runs)')

    # parse arguments and call run_filter
    args = parser.parse_args()
    image_filter = args.gray if args.gray else args.sepia
    if not args.out:
        args.out = f"{args.file}_{image_filter}.jpg"  # Naive. Doesn't remove the original file extension nor the path but oh well. I'm lazy
    
    # Bonus task. Implement runtime flag
    if args.runtime:
        image = read_image(args.file)
        if args.scale != 1:
            image = image.resize((image.width // args.scale, image.height // args.scale))
        runtime = time_one(get_filter(image_filter, args.implementation), image, calls=3)
        print(f"Average time over 3 runs: {runtime / 1_000_000_000:.2f}s")

    run_filter(
        file=args.file,
        out_file=args.out,
        implementation=args.implementation,
        filter=image_filter,
        scale=args.scale
    )
