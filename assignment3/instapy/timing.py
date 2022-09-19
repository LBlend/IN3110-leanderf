"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""
from __init__ import get_filter
from instapy.io import read_image
import numpy as np
import time
from typing import Callable


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable): The filter function to time
        *arguments: Arguments to pass to filter_function
        calls (int): The number of times to call the function, for measurement
    Returns:
        time (float): The average time (in seconds) to run filter_function(*arguments)
    """
    timings = []
    for _ in range(calls):
        t = time.time_ns()
        filter_function(*arguments)
        runtime = (time.time_ns() - t)
        timings.append(runtime)

    return np.average(timings)


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """

    report_output = ""

    # load the image
    image = read_image(filename)

    # print the image name, width, height
    report_image_data = f"Timing performed using {filename}: {image.shape[1]}x{image.shape[0]}\n"
    report_output += f"{report_image_data}\n"
    print(report_image_data)

    # iterate through the filters
    filter_names = ["color2gray"]
    # filter_names = ["color2gray", "color2sepia"]
    for filter_name in filter_names:
        # get the reference filter function
        reference_filter = get_filter(filter_name, implementation="python")

        # time the reference implementation
        reference_time = time_one(reference_filter, image, calls=calls)

        report_reference_data = f"Reference (pure Python) filter time {filter_name}: {int(reference_time) / 1_000_000_000:.3}s ({calls=})"
        report_output += f"{report_reference_data}\n"
        print(report_reference_data)
        
        # iterate through the implementations
        implementations = ["numpy", "numba"]
        for implementation in implementations:
            filter = get_filter(filter_name, implementation=implementation)
            filter_time = time_one(filter, image, calls=calls)
            
            # compare the reference time to the optimized time
            speedup = reference_time / filter_time

            report_implementation_result = f"Timing: {implementation} {filter_name}: {int(filter_time) / 1_000_000_000:.3}s ({speedup=:.2f}x)"
            report_output += f"{report_implementation_result}\n"
            print(report_implementation_result)

        report_output += '\n'
        print('\n')

    # save to file
    with open("timing-report.txt", 'w', encoding='utf-8') as f:
        f.write(report_output)


if __name__ == "__main__":
    # run as `python -m instapy.timing`
    make_reports()
