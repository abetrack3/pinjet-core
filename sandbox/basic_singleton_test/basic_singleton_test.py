from pinjet.core.annotations.injectable import injectable
from pinjet.core.resolver.dependency_resolver import DependencyResolver


@injectable
class SingletonClassToBeResolved:

    pass


resolved_singleton = DependencyResolver.resolve(SingletonClassToBeResolved)

another_singleton = DependencyResolver.resolve(SingletonClassToBeResolved)

if resolved_singleton is another_singleton:

    print("Singleton resolved")

else:

    print("Singleton not resolved")

