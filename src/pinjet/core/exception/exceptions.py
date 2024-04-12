from typing import Callable

from pinjet.common.constants import String
from pinjet.core.constants.element_type import ElementType


class UnregisteredDependencyException(Exception):
    pass


class CircularDependencyException(Exception):
    pass


class UnspecifiedDependencyTypeException(Exception):
    pass


class MultipleProviderForDependencyResolution(Exception):
    pass


class DuplicateSingletonInstanceException(Exception):
    pass


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
