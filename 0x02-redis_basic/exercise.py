#!/usr/bin/env python3
""" This module writes string to Redis """
import redis
import uuid
from typing import Union


class Cache:
    """ This class takes a data argument and 
    returns a string.
    """
    def __init__(self):
        """
        Initialize the Cache class and flush the Redis database.
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:        
        """
        Store the data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The key under which the data is stored in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
