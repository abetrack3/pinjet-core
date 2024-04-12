from strenum import StrEnum


class ElementType(StrEnum):
    CLASS = 'class'
    FUNCTION = 'function'
    STATIC_METHOD = FUNCTION  # haven't found any way to programmatically distinguish these two
    INSTANCE_METHOD = 'instance_method'
    CLASS_METHOD = 'class_method'
    UNDETERMINED = 'undetermined'
