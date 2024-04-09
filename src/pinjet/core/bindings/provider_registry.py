from typing import Dict, Type, Union

from ..types.generic_types import T
from ..types.resolution_procedure import ResolutionProcedure


class ProviderMappings:

    def __init__(self):
        if not hasattr(self, '_mappings'):
            self._mappings: Dict[Union[Type, Type[T]], ResolutionProcedure] = {}

    def __new__(cls):
        if not hasattr(cls, '_singleton_instance'):
            setattr(cls, '_singleton_instance', super(ProviderMappings, cls).__new__(cls))
        return getattr(cls, '_singleton_instance')

    @staticmethod
    def __get_singleton_instance() -> 'ProviderMappings':
        return ProviderMappings()

    @staticmethod
    def put(clazz: Union[Type, Type[T]], source: ResolutionProcedure) -> None:
        ProviderMappings.__get_singleton_instance()._mappings[clazz] = source

    @staticmethod
    def get_source_class(clazz: Union[Type, Type[T]]) -> Union[Type, Type[T]]:
        return ProviderMappings.__get_singleton_instance()._mappings.get(clazz).source_class

    @staticmethod
    def get_source_function_name(clazz: Union[Type, Type[T]]) -> str:
        return ProviderMappings.__get_singleton_instance()._mappings.get(clazz).source_function_name

    @staticmethod
    def contains_resolver_for(clazz: Union[Type, Type[T]]) -> bool:
        return True if clazz in ProviderMappings.__get_singleton_instance()._mappings else False
