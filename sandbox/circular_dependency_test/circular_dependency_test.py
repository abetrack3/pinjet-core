from pinjet.core.annotations.injectable import injectable
from pinjet.core.resolver.dependency_resolver import DependencyResolver


@injectable
class Class1:
    pass


@injectable
class Class2:
    pass


@injectable
class Class3:
    pass


def init_1(self, a: Class2):
    self.a = a


def init_2(self, b: Class3):
    self.b = b


def init_3(self, c: Class1):
    self.c = c


Class1.__init__ = init_1
Class2.__init__ = init_2
Class3.__init__ = init_3


resolved_instance = DependencyResolver.resolve(Class1)

