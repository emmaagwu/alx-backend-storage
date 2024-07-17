#!/usr/bin/env python3
""" This module fetches and caches web pages with access tracking """
import requests
import redis
from functools import wraps
from typing import Callable


def cache_result(expiration: int = 10) -> Callable:
    """
    Decorator to cache the result of a function call in Redis.

    Args:
        expiration (int): The expiration time of the cache in seconds.

    Returns:
        Callable: The decorated function.
    """
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(*args, **kwargs):
            url = args[0]
            cache_key = f"cache:{url}"
            redis_client = redis.Redis()

            # Check if the result is already in the cache
            cached_result = redis_client.get(cache_key)
            if cached_result:
                return cached_result.decode('utf-8')

            # Call the original method to get the result
            result = method(*args, **kwargs)

            # Store the result in the cache with an expiration time
            redis_client.setex(cache_key, expiration, result)

            return result
        return wrapper
    return decorator


def track_access(method: Callable) -> Callable:
    """
    Decorator to track the number of times a URL is accessed.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]
        access_key = f"count:{url}"
        redis_client = redis.Redis()

        # Increment the access count for the URL
        redis_client.incr(access_key)

        return method(*args, **kwargs)
    return wrapper


@cache_result(expiration=10)
@track_access
def get_page(url: str) -> str:
    """
    Get the HTML content of a URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
