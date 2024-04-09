from typing import Dict, Type

from ..exception.exceptions import DuplicateSingletonInstanceException
from ..types.generic_types import T


class SingletonBucket:

    def __init__(self):
        if not hasattr(self, '_bucket'):
            self._bucket: Dict[Type[T], T] = {}

    def __new__(cls):
        if not hasattr(cls, '_singleton_instance'):
            setattr(cls, '_singleton_instance', super(SingletonBucket, cls).__new__(cls))
        return getattr(cls, '_singleton_instance')

    @staticmethod
    def __get_singleton_instance() -> 'SingletonBucket':
        return SingletonBucket()

    @staticmethod
    def put(key: Type[T], value: T) -> None:
        singleton_object = SingletonBucket.__get_singleton_instance()._bucket.setdefault(key, value)
        if value is not singleton_object:
            raise DuplicateSingletonInstanceException

    @staticmethod
    def get(key: Type[T]) -> T:
        return SingletonBucket.__get_singleton_instance()._bucket.get(key)

    @staticmethod
    def contains_singleton(key: Type) -> bool:
        return SingletonBucket.__get_singleton_instance()._bucket.get(key) is not None
