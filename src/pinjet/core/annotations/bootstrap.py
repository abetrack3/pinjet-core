from functools import wraps
from typing import Callable, Any

from .target import target
from ..constants.element_type import ElementType
from ..resource_scanner.resource_scanner import RepositoryScanner


@target(ElementType.FUNCTION)
def pinjet_application(function: Callable) -> Callable:

    @wraps(function)
    def decorated_function(*args, **kwargs) -> Any:

        RepositoryScanner.scan_repository(function)

        result: Any = function(*args, **kwargs)

        return result

    return decorated_function
