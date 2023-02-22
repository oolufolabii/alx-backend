#!/usr/bin/python3
"""Python Module for LIFO caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """An object that stores and retrieve items from
    a dictionary, using LIFO algorithm, until
    a limit is reached"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds data to the cache"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Returns data by key from the cache"""
        return self.cache_data.get(key, None)
