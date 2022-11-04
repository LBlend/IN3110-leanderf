from typing import List  # isort:skip
from collections import deque
from requesting_urls import get_html
from filter_urls import find_articles
import bs4


def compile_path(parents: dict, finish: str) -> List[str]:
    """Returns a path from the start to the finish based on a dictionary of parents

    Arguments:
      parents (dict[str, str]): dictionary containing a wikipedia url and its parent url
      finish (str): wikipedia article URL we want to find a path to

    Returns:
      path (list[str]): the path from the specified start to a node with no parent (starting node)
    """
    current_node = finish
    path = []
    while current_node:
        path.append(current_node)
        current_node = parents[current_node]

    return path[::-1]

def find_path(start: str, finish: str) -> List[str]:
    """Find the shortest path from `start` to `finish`

    Arguments:
      start (str): wikipedia article URL to start from
      finish (str): wikipedia article URL to stop at

    Returns:
      urls (list[str]):
        List of URLs representing the path from `start` to `finish`.
        The first item should be `start`.
        The last item should be `finish`.
        All items of the list should be URLs for wikipedia articles.
        Each article should have a direct link to the next article in the list.
    """

    # Not winning any prize for this one hehe
    # This takes damn long to run but it works

    queue = deque([(start, 0)])
    parents = {start: None}
    visited = set()

    while queue:
        current, depth = queue.popleft()
        visited.add(current)
        
        print(depth, current)

        if current == finish:
            parents[neighbour] = current
            break

        html = get_html(current)
        # Attempt to filter a couple of links to speed it up atleast a little bit
        parser = bs4.BeautifulSoup(html, "html.parser")
        html = str(parser.find(id="mw-content-text"))

        # Get neightbours
        neighbours = find_articles(html)

        for neighbour in neighbours:
            if neighbour in visited:
                continue
            else:
                parents[neighbour] = current
                queue.append((neighbour, depth + 1))

    path = compile_path(parents, finish)

    assert path[0] == start
    assert path[-1] == finish
    return path


if __name__ == "__main__":
    start = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    finish = "https://en.wikipedia.org/wiki/Peace"
    path = find_path(start, finish)
    print("-"*50, ", ".join(path), sep="\n")
