#!/usr/bin/env python3
import uuid
import redis
from typing import Union


class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        """
        Initialize the Cache instance with a Redis client and flush  database.

        Args:
            host (str): Redis server hostname or IP address.
            port (int): Redis server port.
            db (int): Redis database index.
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a randomly generated key and
        return key.

        Args:
            data (Union[str, bytes, int, float]): Data to be stored in Redis.

        Returns:
            str: Randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve a string value from Redis using the provided key.

        Args:
            key (str): The key associated with the value in Redis.

        Returns:
            Union[str, None]: The string value retrieved from Redis,
            or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve an integer value from Redis using the provided key.

        Args:
            key (str): The key associated with the value in Redis.

        Returns:
            Union[int, None]: The integer value retrieved from Redis,
            or None if the key does not exist.
        """
        return self.get(key, fn=int)
