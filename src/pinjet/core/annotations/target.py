import inspect
import functools
from typing import List, Callable

from pinjet.common.constants import Index, Integer

from ..exception.exceptions import TargetElementTypeMisMatchException, TargetTypeNotSpecifiedException
from ..constants.element_type import ElementType


def target(declared_target_element_type):

    if declared_target_element_type is None or not isinstance(declared_target_element_type, ElementType):

        raise TargetTypeNotSpecifiedException

    elif (isinstance(declared_target_element_type, ElementType)
          and declared_target_element_type == ElementType.UNDETERMINED):

        raise ValueError('Target type cannot be undetermined')

    def decorator(target_decorator):

        @functools.wraps(target_decorator)
        def wrapper(*args, **kwargs):

            # Check if the target_decorator accepts its own arguments
            if args and callable(args[Index.ZERO]):

                # If args[0] is a callable, it's likely a function or method
                element_type = __detect_element_type(args[Index.ZERO])

                if element_type != declared_target_element_type:
                    raise TargetElementTypeMisMatchException(target_decorator,
                                                             declared_target_element_type,
                                                             element_type)

            else:

                # Check if the target_decorator is applied to an element
                if len(args) > 1:

                    element_type = __detect_element_type(args[Index.ONE])

                    if element_type != declared_target_element_type:
                        raise TargetElementTypeMisMatchException(target_decorator,
                                                                 declared_target_element_type,
                                                                 element_type)

            # Call the target_decorator
            return target_decorator(*args, **kwargs)

        return wrapper

    return decorator


def __is_class_method(element: Callable, args: List[str]) -> bool:

    if isinstance(element, classmethod):
        return True

    if len(args) != Integer.ZERO and args[Index.ZERO] == 'cls':
        return True

    return False


def __is_instance_method(args: List[str]) -> bool:

    if len(args) != Integer.ZERO and args[Index.ZERO] == 'self':
        return True

    return False


def __detect_element_type(element) -> ElementType:

    if isinstance(element, type):

        return ElementType.CLASS

    elif hasattr(element, '__call__'):

        element_arguments = inspect.getfullargspec(element).args

        if __is_class_method(element, element_arguments):

            return ElementType.CLASS_METHOD

        elif __is_instance_method(element_arguments):

            return ElementType.INSTANCE_METHOD

        elif inspect.isfunction(element):

            return ElementType.FUNCTION

        else:

            return ElementType.UNDETERMINED
