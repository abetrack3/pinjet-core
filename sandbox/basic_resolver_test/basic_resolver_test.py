from pinjet.core.resolver.dependency_resolver import DependencyResolver
from pinjet.core.annotations.injectable import injectable


@injectable
class Class1:

    pass


class1_instance = DependencyResolver.resolve(Class1)

print(type(class1_instance))

