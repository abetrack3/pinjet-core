import unittest
from pinjet.core.annotations.injectable import injectable
from pinjet.core.constants.dependency_scope import DependencyScope
from pinjet.core.resolver.dependency_resolver import DependencyResolver


@injectable(scope=DependencyScope.PROTOTYPE)
class PrototypeClassToBeResolved:
    pass


class BasicPrototypeTest(unittest.TestCase):

    def test_basic_prototype(self):

        # Act
        resolved_instance_1 = DependencyResolver.resolve(PrototypeClassToBeResolved)
        resolved_instance_2 = DependencyResolver.resolve(PrototypeClassToBeResolved)

        # Assert
        self.assertIsNot(resolved_instance_1, resolved_instance_2)


if __name__ == '__main__':
    print('Basic Prototype Test')
    unittest.main()
