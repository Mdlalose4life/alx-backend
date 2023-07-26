#!/usr/bin/env python3
"""A class FIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        """Inherits the methods from BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """Args:
            key(type): _descriptor_
            item(type): _descriptor_
        """
        if key is None or item is None:
            pass
        else:
            # Length of the catch must not exceed the limits
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data.keys():
                # Find the first element on the catch
                oldest_key = next(iter(self.cache_data.keys()))
                # Delete that first element
                del self.cache_data[oldest_key]
                print("DISCAR: {}". format(oldest_key))

            self.cache_data[key] = item


    
    def get(self, key):
        """
            Args:
                key(type): _descriptor_
        """
        if key is None or key not in self.cache_data.keys():
            return None
            
        return self.cache_data.get(key)