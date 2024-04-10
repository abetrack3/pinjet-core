import unittest
from pinjet.core.annotations.injectable import injectable
from pinjet.core.resolver.dependency_resolver import DependencyResolver
from pinjet.core.exception.exceptions import CircularDependencyException


@injectable
class Class1:
    pass


@injectable
class Class2:
    pass


@injectable
class Class3:
    pass


def init_0(self):
    """
    Empty/Default Constructor with no dependencies
    :param self:
    :return:
    """
    pass


def init_1(self, a: Class2):
    self.a = a


def init_2(self, b: Class3):
    self.b = b


def init_3(self, c: Class1):
    self.c = c


class TestCircularDependency(unittest.TestCase):

    def test_resolve_no_circular_dependency(self):

        # Arrange
        Class1.__init__ = init_1
        Class2.__init__ = init_2
        Class3.__init__ = init_0

        # Act
        resolved_instance = DependencyResolver.resolve(Class1)

        # Assert
        self.assertIsInstance(resolved_instance, Class1)

    def test_resolve_circular_dependency(self):

        # Arrange
        Class1.__init__ = init_1
        Class2.__init__ = init_2
        Class3.__init__ = init_3

        # Act & Assert
        with self.assertRaises(CircularDependencyException):
            DependencyResolver.resolve(Class1)


if __name__ == '__main__':
    print('Circular Dependency Test')
    unittest.main()
