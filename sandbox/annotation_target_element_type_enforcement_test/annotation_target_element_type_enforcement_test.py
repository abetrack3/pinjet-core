from pinjet.core.annotations.target import target
from pinjet.core.constants.element_type import ElementType
from pinjet.core.exception.exceptions import AnnotationTargetTypeMismatchException


####################### Happy cases Start #######################


@target(ElementType.FUNCTION)
def simple_method_decorator(method):
    def decorator(*args, **kwargs):
        print('Calling decorated method. Start')

        method(*args, **kwargs)

        print('Calling decorated method. End')

    return decorator


@simple_method_decorator
def sample_method_to_be_decorated():
    print('Inside sample_method_to_be_decorated')


sample_method_to_be_decorated()


@target(ElementType.CLASS)
def simple_class_decorator(clazz):
    print('Inside simple_class_decorator. Start')

    print(clazz)

    print('Inside simple_class_decorator. End')


@simple_class_decorator
class SampleClassToBeDecorated:
    pass


####################### Happy cases End #######################


####################### Error cases Start #######################


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
except AnnotationTargetTypeMismatchException:
    print('Caught annotation target type mismatch')


@target(ElementType.FUNCTION)
def simple_class_decorator(clazz):
    print('Inside simple_class_decorator. Start')

    print(clazz)

    print('Inside simple_class_decorator. End')


try:

    @simple_class_decorator
    class SampleClassToBeDecorated:
        pass

except AnnotationTargetTypeMismatchException:
    print('Caught annotation target type mismatch')

####################### Error cases Start #######################
