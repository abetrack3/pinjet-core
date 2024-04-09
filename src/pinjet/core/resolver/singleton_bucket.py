from threading import RLock
from typing import Dict, Type

from ..exception.exceptions import DuplicateSingletonInstanceException
from ..types.generic_types import T


class SingletonBucket:

    __lock = RLock()

    def __init__(self):
        with SingletonBucket.__lock:
            if not hasattr(self, '__bucket'):
                self.__bucket: Dict[Type[T], T] = {}

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
        with SingletonBucket.__lock:
            singleton_object = SingletonBucket.__get_singleton_instance().__bucket.setdefault(key, value)
            if value is not singleton_object:
                raise DuplicateSingletonInstanceException

    @staticmethod
    def get(key: Type[T]) -> T:
        return SingletonBucket.__get_singleton_instance().__bucket.get(key)

    @staticmethod
    def contains_singleton(key: Type[T]) -> bool:
        return SingletonBucket.__get_singleton_instance().__bucket.get(key) is not None
