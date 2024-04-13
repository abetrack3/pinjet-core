import inspect
from inspect import Parameter
from typing import Type, Set, Dict
from threading import Lock

from ..bindings.provider_registry import ProviderMappings
from ..bindings.registry import DependencyMappings
from ..constants.dependency_scope import DependencyScope
from ..exception.exceptions import (
    UnregisteredDependencyException,
    CircularDependencyException,
    UnspecifiedDependencyTypeException,
)
from ..resolver.singleton_bucket import SingletonBucket
from ..types.generic_types import T
from pinjet.common.constants import Index


class DependencyResolver:

    __lock: Lock = Lock()

    def __new__(cls):
        with DependencyResolver.__lock:
            if not hasattr(DependencyResolver, "__singleton_instance"):
                setattr(cls, '__singleton_instance', super(DependencyResolver, cls).__new__(cls))
        return getattr(cls, '__singleton_instance')

    @staticmethod
    def resolve(clazz: Type[T]) -> T:

        resolver = DependencyResolver.__get_singleton_instance()

        with DependencyResolver.__lock:

            contextual_dependency_set: Set[Type] = set()

            return resolver.__resolve_dependency(clazz, contextual_dependency_set)

    @staticmethod
    def __get_singleton_instance() -> 'DependencyResolver':
        return DependencyResolver()

    def __resolve_dependency(self, clazz: Type[T], contextual_dependency_set: Set[Type]) -> T:

        if self.__is_resolvable(clazz) is not True:
            raise UnregisteredDependencyException(clazz)

        if ProviderMappings.contains_resolver_for(clazz):
            return self.__resolve_by_provided_procedure(clazz, contextual_dependency_set)

        scope: DependencyScope = DependencyMappings.get_scope(clazz)
        implementation = DependencyMappings.get_binding(clazz)

        if implementation in contextual_dependency_set:
            raise CircularDependencyException(implementation)
        else:
            contextual_dependency_set.add(implementation)

        if scope is DependencyScope.SINGLETON and SingletonBucket.contains_singleton(implementation):

            return SingletonBucket.get(implementation)

        dependency_dictionary: Dict[str, Type] = {}

        for parameter_name, parameter_type in inspect.signature(clazz.__init__).parameters.items():

            if self.__parameter_is_skippable(parameter_name, parameter_type):
                continue

            if parameter_type.annotation is Parameter.empty:
                raise UnspecifiedDependencyTypeException(
                    f'Missing type for Constructor parameter: {parameter_name}'
                )

            dependency_dictionary[parameter_name] = self.__resolve_dependency(
                parameter_type.annotation,
                contextual_dependency_set
            )

        resolved = implementation(**dependency_dictionary)

        if scope is DependencyScope.SINGLETON:
            SingletonBucket.put(implementation, resolved)

        contextual_dependency_set.remove(implementation)

        return resolved

    def __resolve_by_provided_procedure(self, clazz: Type[T], contextual_dependency_set: Set[Type]) -> T:

        if clazz in contextual_dependency_set:
            raise CircularDependencyException(clazz)
        else:
            contextual_dependency_set.add(clazz)

        if SingletonBucket.contains_singleton(clazz):
            return SingletonBucket.get(clazz)

        source_class: Type[T] = ProviderMappings.get_source_class(clazz)
        source_class_instance = self.__resolve_dependency(source_class, contextual_dependency_set)

        source_function_name: str = ProviderMappings.get_source_function_name(clazz)
        source_function = [
            (name, member)
            for name, member in inspect.getmembers(source_class_instance)
            if name == source_function_name
        ][Index.ZERO][Index.LAST]

        resolved_instance: T = source_function()

        SingletonBucket.put(clazz, resolved_instance)

        contextual_dependency_set.remove(clazz)

        return resolved_instance

    @staticmethod
    def __is_resolvable(clazz: Type) -> bool:

        if DependencyMappings.contains_binding_for(clazz):
            return True

        if ProviderMappings.contains_resolver_for(clazz):
            return True

        return False

    @staticmethod
    def __parameter_is_skippable(parameter_name: str, parameter_type: Parameter) -> bool:

        if parameter_name == 'self':
            return True

        if parameter_name == 'cls':
            return True

        if parameter_name == 'args' and parameter_type.annotation == Parameter.empty:
            return True

        if parameter_name == 'kwargs' and parameter_type.annotation == Parameter.empty:
            return True

        return False
