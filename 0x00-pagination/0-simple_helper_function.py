#!/usr/bin/env python3
"""A function named index_range that takes two integer arguments
page and page_size. The function should return a tuple of size two
containing a start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination parameters.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returna the start and the end index corespondind to the range of
    """
    # On page 1, you'd show iterms from index 0 to index 9.
    # On page 2, you'd show iterms from index 10 to index 19
    # On page 3, you'd show iterms from index 20 to index 29
    return ((page-1) * page_size, page_size * page)
