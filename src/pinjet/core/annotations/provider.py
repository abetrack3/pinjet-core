import inspect
from inspect import Signature, Parameter
from typing import Type, Callable, Dict, List

from .target import target
from ..bindings.provider_registry import ProviderMappings
from ..constants.element_type import ElementType
from ..exception.exceptions import (
    UnspecifiedDependencyTypeException,
    MultipleProviderForDependencyResolution,
)
from ..annotations.injectable import injectable
from ..types.resolution_procedure import ResolutionProcedure


@target(ElementType.INSTANCE_METHOD)
def provides(function: Callable) -> Callable:

    properties: Dict = vars(function)

    decorator_list: List[Callable] = properties.setdefault('applied_decorators', [])

    if provides not in decorator_list:
        decorator_list.append(provides)

    return function


@target(ElementType.CLASS)
def provider(clazz: Type) -> Type:

    injectable(clazz)

    members = inspect.getmembers(clazz)

    for name, member in members:

        if inspect.isfunction(member) is not True:
            continue

        member_properties: Dict = vars(member)
        applied_decorator_list: List[Callable] = member_properties.setdefault('applied_decorators', [])

        if provides in applied_decorator_list:

            signature: Signature = inspect.signature(member)
            target_instance_type: Type = signature.return_annotation

            if target_instance_type is None or target_instance_type is Parameter.empty:
                raise UnspecifiedDependencyTypeException(f'Missing return type in Provider method: {name}')

            if ProviderMappings.contains_resolver_for(target_instance_type):
                raise MultipleProviderForDependencyResolution(target_instance_type)

            resolution_procedure: ResolutionProcedure = ResolutionProcedure(source_class=clazz,
                                                                            source_function_name=name)

            ProviderMappings.put(target_instance_type, resolution_procedure)

    return clazz
