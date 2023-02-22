#!/usr/bin/python3
"""Python Module for FIFO caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """An object that stores and retrieve items from
    a dictionary, using FIFO algorithm, until
    a limit is reached"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds data to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Returns data from the cache"""
        return self.cache_data.get(key, None)
