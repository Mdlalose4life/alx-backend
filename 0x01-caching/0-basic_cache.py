#!/usr/bin/env python3
"""
"""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()

    def put(self, key, item):
        """
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item


    def get(self, key):
        """
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
