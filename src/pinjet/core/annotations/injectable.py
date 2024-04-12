from typing import Type, Union, Callable

from .target import target
from ..bindings.registry import DependencyMappings
from ..constants.element_type import ElementType
from ..constants.dependency_scope import DependencyScope


@target(ElementType.CLASS)
def injectable(cls: Type = None,
               scope: DependencyScope = DependencyScope.SINGLETON) -> Union[Type, Callable[[Type], Type]]:
    """

    A decorator to register classes as injectable

    :param cls: The class to be registered in the dependency registry
    :param scope: Lifespan of instance - multiple or single
    :return: the registered class or the decorated function that will register the class
    """

    if cls is not None:

        if isinstance(cls, DependencyScope) is False:
            DependencyMappings.bind(cls, cls, scope)
            return cls
        else:
            scope = cls

    def injectable_decorator(clazz: Type) -> Type:

        DependencyMappings.bind(clazz, clazz, scope)

        return clazz

    return injectable_decorator
