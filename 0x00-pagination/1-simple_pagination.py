#!/usr/bin/env python3
"""A function named index_range that takes two integer arguments
page and page_size. The function should return a tuple of size two
containing a start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination parameters.
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returna the start and the end index corespondind to the range of
    """
    # On page 1, you'd show iterms from index 0 to index 9.
    # On page 2, you'd show iterms from index 10 to index 19
    # On page 3, you'd show iterms from index 20 to index 29
    return ((page-1) * page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page that takes two integer arguments page with default value 1
        and page_size with default value 10.
        1. You have to use this CSV file (same as the one presented at the
        top of the project)
        2. Use assert to verify that both arguments are integers
        greaterthan 0.
        3. Use index_range to find the correct indexes to paginate
        the dataset correctly and return the appropriate page of the
        dataset (i.e. the correct list of rows).
        4. If the input arguments are out of range for the dataset,
        an empty list should be returned.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()

        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []
