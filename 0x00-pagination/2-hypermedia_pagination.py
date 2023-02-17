#!/usr/bin/env python3

"""Python module for a Simple Pagination"""

from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the index range from a given page and page size"""

    first_index = (page - 1) * page_size
    last_index = first_index + page_size

    return(first_index, last_index)


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
        """Returns a page from a csv data"""

        assert type(page) == int and type(page_size) == int
        assert page_size > 0 and page > 0
        first_index, last_index = index_range(page, page_size)
        query_data = self.dataset()
        if first_index > len(query_data):
            return []
        return query_data[first_index:last_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns information/data from a page"""

        query_data = self.get_page(page, page_size)
        first_index, last_idx = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset)/page_size)
        page_data_info = {
            'page_size': len(query_data),
            'page': page,
            'data': query_data,
            'next_page': page + 1 if last_idx < len(self.__dataset) else None,
            'prev_page': page - 1 if first_index > 0 else None,
            'total_pages': total_pages,
        }
        return page_data_info
