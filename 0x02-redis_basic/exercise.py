#!/usr/bin/env python3
""" This module writes string to Redis """
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """ This class takes a data argument and returns a string.
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

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Optional[Union[str, bytes, int, float]]:
        """
        Retrieve the data from Redis and optionally
            apply a conversion function.

        Args:
            key (str): The key under which the data is stored in Redis.
            fn (Optional[Callable]): The conversion function
                 to apply to the data.

        Returns:
            Optional[Union[str, bytes, int, float]]: The retrieved
              data, optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the data as a string from Redis.

        Args:
            key (str): The key under which the data is stored in Redis.

        Returns:
            Optional[str]: The retrieved data as a string.
        """
        return self.get(key, lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the data as an integer from Redis.

        Args:
            key (str): The key under which the data is stored in Redis.

        Returns:
            Optional[int]: The retrieved data as an integer.
        """
        return self.get(key, lambda data: int(data))
