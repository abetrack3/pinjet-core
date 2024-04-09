from typing import Type, Dict

from ..constants.dependency_scope import DependencyScope
from ..types.generic_types import T
from pinjet.common.constants import String


class DependencyMappings:

    def __init__(self):
        if not hasattr(self, '_mappings'):
            self._mappings: Dict[Type, Type] = {}
        if not hasattr(self, '_scope_mappings'):
            self._scope_mappings: Dict[Type, DependencyScope] = {}

    def __new__(cls):

        if not hasattr(cls, 'singleton_instance'):
            setattr(cls, 'singleton_instance', super(DependencyMappings, cls).__new__(cls))
        return getattr(cls, 'singleton_instance')

    @staticmethod
    def __get_singleton_instance() -> 'DependencyMappings':
        return DependencyMappings()

    @staticmethod
    def bind(key: Type, value: Type, scope=DependencyScope.SINGLETON) -> None:
        DependencyMappings.__get_singleton_instance()._mappings[key] = value
        DependencyMappings.__get_singleton_instance()._scope_mappings[key] = scope

    @staticmethod
    def get_binding(key: Type[T]) -> Type[T]:
        return DependencyMappings.__get_singleton_instance()._mappings.get(key)

    @staticmethod
    def get_scope(key: Type) -> DependencyScope:
        return DependencyMappings.__get_singleton_instance()._scope_mappings.get(key)

    @staticmethod
    def contains_binding_for(key: Type) -> bool:
        return True if key in DependencyMappings.__get_singleton_instance()._mappings else False

    def __str__(self) -> str:
        return f'class_mappings {str(self._mappings)}' \
               f'{String.NEXT_LINE}' \
               f'scope_mappings {str(self._scope_mappings)}'
