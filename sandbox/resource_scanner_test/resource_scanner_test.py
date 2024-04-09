from argparse import ArgumentParser

from pinjet.core.annotations.bootstrap import pinjet_application
from pinjet.core.resolver.dependency_resolver import DependencyResolver


print('before pinjet_application')

@pinjet_application
def __main__():
    parser = DependencyResolver.resolve(ArgumentParser)

    print(parser)

print('after pinjet_application')

if __name__ == '__main__':
    print('Resource scanner test')

    __main__()

print('Resource scanner test')