#!/usr/bin/env python3

"""Python module for a Simple Helper Function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the index range from a given page and page size"""

    first_index = (page - 1) * page_size
    last_index = first_index + page_size

    return(first_index, last_index)
