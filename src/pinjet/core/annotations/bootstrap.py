from typing import Callable, Any

from ..resource_scanner.resource_scanner import RepositoryScanner


def pinjet_application(function: Callable) -> Callable:

    def decorated_function(*args, **kwargs) -> Any:

        RepositoryScanner.scan_repository(function)

        result: Any = function(*args, **kwargs)

        return result

    return decorated_function
