from functools import wraps
from typing import Callable

from pinjet.core.annotations.target import target
from pinjet.core.constants.element_type import ElementType
from pinjet.core.exception.exceptions import TargetElementTypeMisMatchException


#
# Enforcing decorator to be applied only on functions
#

@target(ElementType.FUNCTION)
def simple_function_decorator(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        print('Calling decorated method. Start')

        result = function(*args, **kwargs)

        print('Calling decorated method. End')

        return result

    return decorator


@simple_function_decorator
def sample_function_to_be_decorated():
    print('Inside sample_method_to_be_decorated')


sample_function_to_be_decorated()


#
# Enforcing decorator to be applied only on functions with parameters
#

@simple_function_decorator
def sample_function_with_parameters_to_be_decorated(message: str):
    return f'message: {message}'


print(sample_function_with_parameters_to_be_decorated(message='hello'))


#
# Enforcing decorators to be applied on class only
#

@target(ElementType.CLASS)
def simple_class_decorator(clazz):
    print('Inside simple_class_decorator. Start')

    print(clazz)

    print('Inside simple_class_decorator. End')

    return clazz


#
# Enforcing decorators to be applied on instance methods only
#

@target(ElementType.INSTANCE_METHOD)
def simple_instance_method_decorator(instance_method):
    @wraps(instance_method)
    def decorator(*args, **kwargs):
        print('Inside instance_method_decorator. Start')

        result = instance_method(*args, **kwargs)

        print('Inside instance_method_decorator. End')

        return result

    return decorator


#
# Enforcing decorators to apply on static methods only
#

@target(ElementType.STATIC_METHOD)
def simple_static_method_decorator(class_static_method):
    @wraps(class_static_method)
    def decorator(*args, **kwargs):
        print('Inside static_method_decorator. Start')

        result = class_static_method(*args, **kwargs)

        print('Inside static_method_decorator. End')

        return result

    return decorator


#
# Enforcing decorators to be used on class methods only
#

@target(ElementType.CLASS_METHOD)
def simple_class_method_decorator(class_method):

    @wraps(class_method)
    def decorator(*args, **kwargs):

        print('Inside class_method_decorator. Start')

        result = class_method(*args, **kwargs)

        print('Inside class_method_decorator. End')

        return result

    return decorator


@simple_class_decorator
class SampleClassToBeDecorated:

    @simple_instance_method_decorator
    def sample_instance_method_to_be_decorated(self):
        return 'inside sample_instance_method_to_be_decorated'

    @staticmethod
    @simple_static_method_decorator
    def sample_static_method_to_be_decorated():
        return 'inside sample_static_method_to_be_decorated'

    @classmethod
    @simple_class_method_decorator
    def sample_class_method_to_be_decorated(cls):
        return 'inside sample_class_method_to_be_decorated'


sample_object = SampleClassToBeDecorated()
print(sample_object.sample_instance_method_to_be_decorated())
print(sample_object.sample_static_method_to_be_decorated())
print(sample_object.sample_class_method_to_be_decorated())


#
# Error case: A method decorator is being declared with target type class
#

@target(ElementType.CLASS)
def simple_method_decorator(method):
    def decorator(*args, **kwargs):
        print('Calling decorated method. Start')

        method(*args, **kwargs)

        print('Calling decorated method. End')

    return decorator


try:
    @simple_method_decorator
    def sample_method_to_be_decorated():
        print('Inside sample_method_to_be_decorated')


    sample_method_to_be_decorated()
except TargetElementTypeMisMatchException as caught_exception:
    print(caught_exception)
    print('Caught annotation target type mismatch')


#
# Error case: a class decorator is being declared with target type function
#

@target(ElementType.FUNCTION)
def simple_class_decorator(clazz):
    print('Inside simple_class_decorator. Start')

    print(clazz)

    print('Inside simple_class_decorator. End')


try:

    @simple_class_decorator
    class SampleClassToBeDecorated:
        pass

except TargetElementTypeMisMatchException as caught_exception:
    print(caught_exception)
    print('Caught annotation target type mismatch')


#
# Error case: a class method decorator is being applied to instance method
#

try:

    @target(ElementType.CLASS_METHOD)
    def simple_class_method_decorator(method: Callable) -> Callable:

        @wraps(method)
        def decorator(*args, **kwargs):
            print('Inside simple_class_method_decorator. Start')

            method(*args, **kwargs)

            print('Inside simple_class_method_decorator. End')

        return decorator


    class SimpleClass:

        @simple_class_method_decorator
        def sample_class_method_to_be_decorated(self):
            print('Inside sample_class_method_to_be_decorated')

except TargetElementTypeMisMatchException as caught_exception:
    print(caught_exception)
    print('Caught annotation target type mismatch')
