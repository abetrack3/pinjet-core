from pinjet.core.annotations.injectable import injectable
from pinjet.core.constants.dependency_scope import DependencyScope
from pinjet.core.resolver.dependency_resolver import DependencyResolver


@injectable(scope=DependencyScope.PROTOTYPE)
class PrototypeClassToBeResolved:
    pass


resolved_instance = DependencyResolver.resolve(PrototypeClassToBeResolved)

print(resolved_instance)

resolved_instance2 = DependencyResolver.resolve(PrototypeClassToBeResolved)

print(resolved_instance2)

if resolved_instance is not resolved_instance2:

    print('successful prototype creation')

else:

    print('failed prototype creation')

