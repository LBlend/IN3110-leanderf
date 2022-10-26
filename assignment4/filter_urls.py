import re

## -- Task 2 -- ##


def find_urls(
    html: str,
    base_url: str = "https://en.wikipedia.org",
    output: str = None,
) -> set:
    """Find all the url links in a html text using regex
    Arguments:
        html (str): html string to parse
    Returns:
        urls (set) : set with all the urls found in html text
    """
    # create and compile regular expression(s)

    #urls = re.findall("(https?:\/\/\w+\.\w+(\w+|[\.%&?\-=+\/])+)|((?<=src=\").+(?=\"))", html)
    # Yes, this is terrible, I know
    normal_urls = re.findall(r"https?:\/\/\w+\.\w+[\w+-=&\/?\.%]*", html)
    #href_urls = re.findall(r"(?<=href=\")[\/|\w|\.|\-|\:]+", html)
    #src_urls = re.findall(r"(?<=src=\")[\/|\w|\.|\-|\:]+", html)
    href_urls = re.findall(r"(?<=href=\")\/+[\/|\.|\-|\:|\w]+", html)
    src_urls = re.findall(r"(?<=src=\")\/+[\/|\.|\-|\:|\w]+", html)

    href_urls = list(map(lambda url: re.sub(r"^\/\/", "https://", url), href_urls))
    href_urls = list(map(lambda url: re.sub(r"^\/.*", base_url + url, url), href_urls))
    
    src_urls = list(map(lambda url: re.sub(r"^\/\/", "https://", url), src_urls))
    src_urls = list(map(lambda url: re.sub(r"^\/.*", base_url + url, url), src_urls))

    tag_urls = href_urls + src_urls
    all_urls = set(normal_urls + tag_urls)

    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        with open(output, "w") as f:
            f.write("\n".join(all_urls))

    return all_urls


def find_articles(html: str, output=None) -> set:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
    returns:
        - (set) : a set with urls to all the articles found
    """
    urls = find_urls(html)
    articles = set(filter(lambda url: re.search(r"https?:\/\/\w+\.\wikipedia.org\/wiki[\w+-=&\/?\.%]*", url), urls))

    # Write to file if wanted
    if output:
        with open(output, "w") as f:
            f.write("\n".join(articles))
    return articles


## Regex example
def find_img_src(html: str):
    """Find all src attributes of img tags in an HTML string

    Args:
        html (str): A string containing some HTML.

    Returns:
        src_set (set): A set of strings containing image URLs

    The set contains every found src attibute of an img tag in the given HTML.
    """
    # img_pat finds all the <img alt="..." src="..."> snippets
    # this finds <img and collects everything up to the closing '>'
    img_pat = re.compile(r"<img[^>]+>", flags=re.IGNORECASE)
    # src finds the text between quotes of the `src` attribute
    src_pat = re.compile(r'src="([^"]+)"', flags=re.IGNORECASE)
    src_set = set()
    # first, find all the img tags
    for img_tag in img_pat.findall(html):
        # then, find the src attribute of the img, if any
        match = src_pat.search(img_tag)
        if match:
            src_set.add(match.group(1))
    return src_set
