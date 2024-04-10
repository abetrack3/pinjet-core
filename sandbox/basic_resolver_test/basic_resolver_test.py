import unittest
from pinjet.core.resolver.dependency_resolver import DependencyResolver
from pinjet.core.annotations.injectable import injectable


class UnregisteredClassToBeResolved:
    pass


@injectable
class InjectableClassToBeResolved:
    pass


class TestDependencyResolver(unittest.TestCase):
    def test_resolve_successful(self):

        # Act
        result = DependencyResolver.resolve(InjectableClassToBeResolved)

        # Assert
        self.assertIsInstance(result, InjectableClassToBeResolved)

    def test_resolve_failed_unregistered_class(self):
        # Act & Assert
        with self.assertRaises(Exception):
            DependencyResolver.resolve(UnregisteredClassToBeResolved)


if __name__ == '__main__':
    print('Basic Resolver Test')
    unittest.main()
