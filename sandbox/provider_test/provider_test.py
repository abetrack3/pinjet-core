from argparse import ArgumentParser

from pinjet.core.annotations.provider import provider, provides
from pinjet.core.resolver.dependency_resolver import DependencyResolver


@provider
class ArgumentParserProvider:

    @provides
    def get_argument_parser(self) -> ArgumentParser:

        argument_parser = ArgumentParser()

        return argument_parser


parser = DependencyResolver.resolve(ArgumentParser)

print(parser)


@provider
class SecondaryArgumentParserProvider:

    @provides
    def get_argument_parser(self) -> ArgumentParser:

        argument_parser = ArgumentParser()

        return argument_parser


parser = DependencyResolver.resolve(ArgumentParser)

print(parser)

