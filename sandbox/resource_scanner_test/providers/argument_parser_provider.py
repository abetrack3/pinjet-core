from argparse import ArgumentParser
from pinjet.core.annotations.provider import provider, provides


@provider
class ArgumentParserProvider:

    @provides
    def get_argument_parser(self) -> ArgumentParser:
        return ArgumentParser()
