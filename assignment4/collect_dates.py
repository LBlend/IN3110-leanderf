import re
from typing import Tuple

## -- Task 3 (IN3110 optional, IN4110 required) -- ##

# create array with all names of months
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

month_abbreviations = list(map(lambda month: month[:3], month_names))


def get_date_patterns() -> Tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """

    # Regex to capture days, months and years with numbers
    # year should accept a 4-digit number between at least 1000-2029
    year = r"(?P<year>\d{4})"

    # month should accept month names or month numbers
    month = rf"(?<!\d)(?P<month>1[0-2]?|0[1-9]|{'|'.join(month_names)}|{'|'.join(month_abbreviations)})(?!\d)"

    # day should be a number, which may or may not be zero-padded
    day = r"(?<!\d)(?P<day>[0-2]{0,1}\d{1}|3[0-1]{1})(?!\d)"

    return year, month, day


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    You don't need to use this function,
    but you may find it useful.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """
    # If already digit do nothing
    if s.isdigit():
        return zero_pad(s)

    # Not a digit. Make sure first letter is capitalized
    s = s.title()

    # Get month number
    if len(s) == 3:
        s = str(month_abbreviations.index(s) + 1)
    else:
        s = str(month_names.index(s) + 1)

    return zero_pad(s)


def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    You don't need to use this function,
    but you may find it useful.
    """
    if len(n) == 1:
        return f"0{n}"

    return n


def find_dates(text: str, output: str = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
    return:
        results (list): A list with all the dates found
    """
    year, month, day = get_date_patterns()

    # Pattern that matches spaces between date segments
    space_pattern = r"[ \/,\-]{1,2}"

    # Date on format YYYY/MM/DD - ISO
    ISO = rf"{year}{space_pattern}{month}{space_pattern}{day}"

    # Date on format DD/MM/YYYY
    DMY = rf"{day}{space_pattern}{month}{space_pattern}{year}"

    # Date on format MM/DD/YYYY
    MDY = rf"{month}{space_pattern}{day}{space_pattern}{year}"

    # Date on format YYYY/MM/DD
    # YMD = ISO
    # YMD is redundant since ISO matches it, hence I've commented it out

    # list with all supported formats
    formats = [DMY, MDY, ISO]
    dates = []

    # find all dates in any format in text
    for pattern in formats:
        found_dates = re.findall(pattern, text, flags=re.IGNORECASE)

        if not found_dates:
            continue

        for date in found_dates:
            # Convert list of match groups to string
            date = " ".join(date)

            # Reorder date to Year Month Day
            date = re.sub(pattern, r"\g<year>/\g<month>/\g<day>", date, flags=re.IGNORECASE)

            # Convert month to number
            date = re.sub(month, lambda m: convert_month(m.group("month")), date, flags=re.IGNORECASE)

            # Zero-pad day
            date = re.sub(day, lambda d: zero_pad(d.group("day")), date, flags=re.IGNORECASE)

            # Add to list
            dates.append(date)

    # Write to file if wanted
    if output:
        with open(output, "w") as f:
            f.write("\n".join(dates))

    return dates
