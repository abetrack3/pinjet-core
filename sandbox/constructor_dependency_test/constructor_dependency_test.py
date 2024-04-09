from pinjet.core.resolver.dependency_resolver import DependencyResolver
from pinjet.core.annotations.injectable import injectable


@injectable
class Class1:

    def __str__(self) -> str:
        return 'Class1->[]'


@injectable
class Class3:

    def __init__(self, a: Class1):
        self.a = a

    def __str__(self) -> str:
        return f'Class3->["self.a":"{self.a}"]'


@injectable
class Class2:

    def __init__(self, a: Class3, b: Class3):
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f'Class2->["self.a":"{self.a}", "self.b":"{self.b}"]'


resolved_instance: Class2 = DependencyResolver.resolve(Class2)

print(resolved_instance)

