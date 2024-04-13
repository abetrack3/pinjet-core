from threading import Lock
from typing import Dict, Type

from ..exception.exceptions import DuplicateSingletonInstanceException
from ..types.generic_types import T


class SingletonBucket:

    __lock = Lock()

    def __init__(self):
        with SingletonBucket.__lock:
            if not hasattr(self, '_bucket'):
                self._bucket: Dict[Type[T], T] = {}

    def __new__(cls):
        with SingletonBucket.__lock:
            if not hasattr(cls, '__singleton_instance'):
                setattr(cls, '__singleton_instance', super(SingletonBucket, cls).__new__(cls))
        return getattr(cls, '__singleton_instance')

    @staticmethod
    def __get_singleton_instance() -> 'SingletonBucket':
        return SingletonBucket()

    @staticmethod
    def put(key: Type[T], value: T) -> None:
        singleton_bucket = SingletonBucket.__get_singleton_instance()
        with SingletonBucket.__lock:
            if key in singleton_bucket._bucket:
                raise DuplicateSingletonInstanceException(key)
            singleton_bucket._bucket[key] = value

    @staticmethod
    def get(key: Type[T]) -> T:
        return SingletonBucket.__get_singleton_instance()._bucket.get(key)

    @staticmethod
    def contains_singleton(key: Type[T]) -> bool:
        return SingletonBucket.__get_singleton_instance()._bucket.get(key) is not None
