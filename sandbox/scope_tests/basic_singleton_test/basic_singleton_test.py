import unittest
from pinjet.core.annotations.injectable import injectable
from pinjet.core.resolver.dependency_resolver import DependencyResolver


@injectable
class SingletonClassToBeResolved:

    pass


class BasicSingletonTest(unittest.TestCase):

    def test_singleton(self):

        # Act
        resolved_singleton_1 = DependencyResolver.resolve(SingletonClassToBeResolved)
        resolved_singleton_2 = DependencyResolver.resolve(SingletonClassToBeResolved)

        # Assert
        self.assertIs(resolved_singleton_1, resolved_singleton_2)


if __name__ == '__main__':
    print('Basic Singleton Test')
    unittest.main()

