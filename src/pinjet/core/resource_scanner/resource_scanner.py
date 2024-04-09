import os
import inspect
from types import ModuleType
from importlib.machinery import ModuleSpec
from importlib.util import spec_from_file_location, module_from_spec
from typing import Callable

from pinjet.common.constants import String
from pinjet.common.constants.io import SKIPPABLE_DIRECTORIES, PYTHON_SCRIPT_EXTENSION


class RepositoryScanner:

    @staticmethod
    def scan_repository(main_function: Callable):

        source_directory: str = os.path.dirname(inspect.getfile(main_function))

        for root, _, files in os.walk(source_directory):

            for file_name in files:

                if not file_name.endswith(PYTHON_SCRIPT_EXTENSION):
                    continue

                file_path = os.path.join(root, file_name)
                module_name = file_name.replace(PYTHON_SCRIPT_EXTENSION, String.EMPTY)

                if any(map(lambda skippable_directory: skippable_directory in file_path, SKIPPABLE_DIRECTORIES)):
                    continue

                loaded_spec: ModuleSpec = spec_from_file_location(module_name, file_path)
                loaded_module: ModuleType = module_from_spec(loaded_spec)
                loaded_spec.loader.exec_module(loaded_module)
