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


class AnnotationTargetTypeMismatchException(Exception):
    pass
