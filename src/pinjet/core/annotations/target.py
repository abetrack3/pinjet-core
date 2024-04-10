import inspect
from typing import Callable, Optional
from functools import wraps

from ..constants.element_type import ElementType
from ..exception.exceptions import TargetTypeNotSpecifiedException, AnnotationTargetTypeMismatchException


def target(element: ElementType) -> Callable:

    if element is None:
        raise TargetTypeNotSpecifiedException

    if not isinstance(element, ElementType):
        raise ValueError(f'Target element {element} is not an instance of AnnotationTargetType')

    def wrapper(target_decorator_function: Callable) -> Callable:

        @wraps(target_decorator_function)
        def decorated(callable_object: Optional[Callable] = None, *args, **kwargs) -> Callable:

            if callable_object is None:
                return target_decorator_function(*args, **kwargs)

            if element is ElementType.FUNCTION and inspect.isfunction(callable_object) is not True:
                raise AnnotationTargetTypeMismatchException

            if element is ElementType.CLASS and inspect.isclass(callable_object) is not True:
                raise AnnotationTargetTypeMismatchException

            if element is ElementType.METHOD and inspect.isfunction(callable_object) is not True:
                raise AnnotationTargetTypeMismatchException

            return target_decorator_function(callable_object, *args, **kwargs)

        return decorated

    return wrapper
