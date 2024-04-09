from dataclasses import dataclass
from typing import Type


@dataclass
class ResolutionProcedure:
    source_class: Type
    source_function_name: str
