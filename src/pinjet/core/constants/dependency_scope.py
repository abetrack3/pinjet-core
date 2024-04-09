from strenum import StrEnum


class DependencyScope(StrEnum):
    SINGLETON = 'singleton'
    FACTORY = 'factory'
