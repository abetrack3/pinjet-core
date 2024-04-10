import unittest
from argparse import ArgumentParser

from pinjet.core.annotations.provider import provider, provides
from pinjet.core.resolver.dependency_resolver import DependencyResolver
from pinjet.core.exception.exceptions import MultipleProviderForDependencyResolution


@provider
class ArgumentParserProvider:

    @provides
    def get_argument_parser(self) -> ArgumentParser:
        argument_parser = ArgumentParser()

        return argument_parser


class ProviderTests(unittest.TestCase):

    def test_single_concrete_provider(self):
        # Act
        argument_parser = DependencyResolver.resolve(ArgumentParser)

        # Assert
        self.assertIsInstance(argument_parser, ArgumentParser)

    def test_multiple_concrete_provider(self):

        # Arrange Act & Assert
        with self.assertRaises(MultipleProviderForDependencyResolution):
            @provider
            class SecondaryArgumentParserProvider:

                @provides
                def get_argument_parser(self) -> ArgumentParser:
                    argument_parser = ArgumentParser()

                    return argument_parser


if __name__ == '__main__':
    print('Provider Test')
    unittest.main()
