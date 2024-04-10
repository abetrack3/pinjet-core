import unittest
from pinjet.core.annotations.injectable import injectable
from pinjet.core.resolver.dependency_resolver import DependencyResolver


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

    def __init__(self, a: Class1, b: Class3):
        self.a: Class1 = a
        self.b: Class3 = b

    def __str__(self) -> str:
        return f'Class2->["self.a":"{self.a}", "self.b":"{self.b}"]'


class TestConstructorDependency(unittest.TestCase):

    def test_constructor_dependency(self):

        # Act
        resolved_instance: Class2 = DependencyResolver.resolve(Class2)

        # Assert
        self.assertIsInstance(resolved_instance, Class2)
        self.assertIsInstance(resolved_instance.a, Class1)
        self.assertIsInstance(resolved_instance.b, Class3)
        self.assertIsInstance(resolved_instance.b.a, Class1)


if __name__ == '__main__':
    print('Constructor Dependency Test')
    unittest.main()
