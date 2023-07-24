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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the following key-value pairs:
        
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        
        Make sure to reuse get_page in your implementation.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        
        data = self.get_page(page, page_size)
        
        #find total pages
        total_pages = math.ceil(len(self.dataset())/ page_size)

        start, end = index_range(page, page_size)

        #find the next page
        if (page < total_pages):
            next_page = page + 1
        else:
            next_page = None

        #Find the previous
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1
            
        return{
            'page_size': len(data),
            'page' : page,
            'data' : data,
            'next_page' : next_page,
            'prev_page' : prev_page,
            'total_pages' : total_pages
        }
