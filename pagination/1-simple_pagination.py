#!/usr/bin/env python3
'''
The function should return a tuple of size two
containing a start index and an end index corresponding
to the range of indexes to return in a
list for those particular pagination parameters.
'''

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


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
        '''get page method'''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page and page_size > 0
        
        indices = index_range(page, page_size)
        start = indices[0]
        end = indices[1]
        
        try:
            return self.dataset()[start:end]
        except IndexError:
            return []
