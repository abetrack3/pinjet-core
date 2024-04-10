import unittest
from argparse import ArgumentParser

from pinjet.core.annotations.bootstrap import pinjet_application
from pinjet.core.resolver.dependency_resolver import DependencyResolver


class ResourceScannerTest(unittest.TestCase):

    def test_resource_scanner(self):

        # Arrange
        @pinjet_application
        def main() -> ArgumentParser:

            return DependencyResolver.resolve(ArgumentParser)

        # Act
        argument_parser = main()

        # Assert
        self.assertIsInstance(argument_parser, ArgumentParser)


if __name__ == '__main__':
    print('Resource Scanner Test')
    unittest.main()
