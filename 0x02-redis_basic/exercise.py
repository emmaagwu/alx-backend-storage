#!/usr/bin/env python3
""" This module writes string to Redis """
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of calls to a method.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Wrapper function that increments the call count in Redis.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ This class takes a data argument and returns a string.
    """
    def __init__(self) -> None:
        """
        Initialize the Cache class and flush the Redis database.
        """

        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
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

    def get(self, key: str, fn: Callable = None,)\
            -> Union[str, bytes, int, float]:
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
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """
        Retrieve the data as a string from Redis.

        Args:
            key (str): The key under which the data is stored in Redis.

        Returns:
            Optional[str]: The retrieved data as a string.
        """
        return self.get(key, lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieve the data as an integer from Redis.

        Args:
            key (str): The key under which the data is stored in Redis.

        Returns:
            Optional[int]: The retrieved data as an integer.
        """
        return self.get(key, lambda data: int(data))
