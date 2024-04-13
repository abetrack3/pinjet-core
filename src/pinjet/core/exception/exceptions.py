from typing import Callable, Type

from pinjet.common.constants import String
from pinjet.core.constants.element_type import ElementType


class UnregisteredDependencyException(Exception):

    def __init__(self, dependency: Type):
        super().__init__(f'Unregistered dependency "{dependency.__qualname__}"')


class CircularDependencyException(Exception):

    def __init__(self, dependency: Type):
        super().__init__(f'Circular dependency "{dependency.__qualname__}"')


class UnspecifiedDependencyTypeException(Exception):

    def __init__(self, message: str = String.EMPTY):
        super().__init__(message)


class MultipleProviderForDependencyResolution(Exception):

    def __init__(self, dependency: Type):
        super().__init__(f'More than one provider method for dependency "{dependency.__qualname__}" detected')


class DuplicateSingletonInstanceException(Exception):

    def __init__(self, singleton_dependency: Type):
        super().__init__(f'Duplicate singleton instance "{singleton_dependency.__qualname__}" detected')


class TargetTypeNotSpecifiedException(Exception):
    pass


class TargetElementTypeMisMatchException(Exception):

    def __init__(self,
                 target_decorator: Callable,
                 declared_element_type: ElementType,
                 received_element_type: ElementType):

        super().__init__(
            f'Target decorator: "{target_decorator.__qualname__}" placed wrongfully.{String.NEXT_LINE}'
            f'Should be applied to of type: "{declared_element_type.upper()}" only.{String.NEXT_LINE}'
            f'But found to be applied to of type: "{received_element_type.upper()}".{String.NEXT_LINE}'
        )
