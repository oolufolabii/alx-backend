#!/usr/bin/python3
"""Python Module on Simple Caching"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """An object to create, store and retrieve data from dictionary"""

    def put(self, key, item):
        """Adds data to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Returns data from the cache"""
        return self.cache_data.get(key, None)
