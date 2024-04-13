# Pinjet
#### Small like a pin, fast like a jet! A lightweight Dependency Injection library for Python

---

## Installation

```shell
pip install pinjet-core
```
---

## Introdcution

Numerous Dependency Injection (DI) frameworks exist for Python, yet none are flawless or intuitive, whether in terms of syntax or programmatically configuring. This led to the creation of Pinjet, a simple and intuitive DI library, that requires minimal or no configuration code at all. Simply annotate your classes and methods with **Pinjet decorators**, and it take cares of the rest. Pinjet follows **annotation-first** approach, drawing inspiration from Java **Spring** and **Spring Boot**, making project initialization as effortless as possible. This approach is particularly beneficial for developers experienced in Java and Spring Boot, easing their transition to **Pinjet** projects.

*In Pinjet, the terms "annotation" and "decorator" are frequently interchanged and carry the same meaning.*

#### Quick Exmaple
```python
from pinjet.core.resolver.dependency_resolver import DependencyResolver
from pinjet.core.annotations.injectable import injectable

@injectable
class InjectableClassToBeResolved:
    pass

result = DependencyResolver.resolve(InjectableClassToBeResolved)

```

Pinjet simplifies the usage by employing `@injectable` to mark any classes requiring injection. Unlike Spring Boot, where figuring out when to use `@Component` or `@Service` can be daunting, Pinjet offers a more straightforward approach.

---

## Customizing Dependency Scope

By default, any class marked with `@injectable` is considered a singleton, ensuring the same instance is returned every time `resolve()` is called. However, if you prefer a new instance on each call to `resolve()`, simply specify the dependency scope as **PROTOTYPE** in `@injectable`.

#### Example
```python

from pinjet.core.annotations.injectable import injectable
from pinjet.core.constants.dependency_scope import DependencyScope
from pinjet.core.resolver.dependency_resolver import DependencyResolver


@injectable(scope=DependencyScope.PROTOTYPE)
class PrototypeClassToBeResolved:
    pass

resolved_instance_1 = DependencyResolver.resolve(PrototypeClassToBeResolved)
resolved_instance_2 = DependencyResolver.resolve(PrototypeClassToBeResolved)

is_different_instance: bool = resolved_instance_1 is not resolved_instance_2 # True
```

---

## Customization with Providers

Pinjet allows customization of class instantiation and resolution via `@provider` and `@provides`. For instance:

```python
from argparse import ArgumentParser
from pinjet.core.annotations.provider import provider, provides
from pinjet.core.resolver.dependency_resolver import DependencyResolver

@provider
class ArgumentParserProvider:

    @provides
    def get_argument_parser(self) -> ArgumentParser:
        argument_parser = ArgumentParser()
        argument_parser.add_argument('--environment', type=str, required=False)
        argument_parser.set_defaults(configuration='development')
        return argument_parser

argument_parser = DependencyResolver.resolve(ArgumentParser)
```

This approach is also applicable when injecting classes from third-party libraries that cannot be modified to include `@injectable`.

---

## Scanning Ahead of Time

For any Python projects where codes are distributed across modules, Pinjet recommends wrapping the program's starting point, which is often, `__main__()` with `@pinjet_application`. This allows Pinjet to:

- scan the repository to identify all dependencies with the help of `@pinjet_application`
- ensuring `DependencyResolver` is primed to serve the application.

#### Example

```python
from argparse import ArgumentParser

from pinjet.core.annotations.bootstrap import pinjet_application
from pinjet.core.resolver.dependency_resolver import DependencyResolver


@pinjet_application
def __main__():

    argument_parser: ArgumentParser = DependencyResolver.resolve(ArgumentParser)


if __name__ == '__main__':
    __main__()
```
Here ArgumentParser is configured to instantiate using `@provider` and `@provides` on a separate module which Pinjet is not aware of, if the program starting point is not marked with `@pinjet_application`

---

## Decorator Type Safety

To enhance developer experience, Pinjet introduces decorator type safety. For example, `@injectable` is exclusively meant for **classes**, while `@pinjet_application` is meant for **functions**. Introducing `@target`, a special decorator, which ensures decorators are applied to their intended elements.

#### Quick Demonstration

```python
from functools import wraps
from pinjet.core.annotations.target import target
from pinjet.core.constants.element_type import ElementType

@target(ElementType.FUNCTION)
def simple_function_decorator(function):

    @wraps(function)
    def decorator(*args, **kwargs):

        result = function(*args, **kwargs)

        return result

    return decorator

@simple_function_decorator
def sample_function_to_be_decorated():
    print('Inside sample_method_to_be_decorated')

sample_function_to_be_decorated() # prints: 'Inside sample_method_to_be_decorated'

```

With `@target` we are now enforcing that the decorator `simple_function_decorator` can only be used on functions. Attempting to use a decorator on an incorrect element type will raise a `TargetElementTypeMisMatchException` with a comprehensive error message.

You can write your own custom decorator and enforce its usage with `@target` as well!

---

## Development Status

Pinjet is in its early stages and under active development. Numerous features are planned for future releases. Suggestions, improvements, and open-source contributions are most welcome. While the project may initially seem small like a pin, it is poised to grow as fast as a jet!

---

# Thank you
