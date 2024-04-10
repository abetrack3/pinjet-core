import time
import unittest
import concurrent.futures
from pinjet.core.annotations.injectable import injectable
from pinjet.core.resolver.dependency_resolver import DependencyResolver


@injectable
class ClassToBeResolved:
    pass


class TestSingletonResolverThreadSafety(unittest.TestCase):

    def test_singleton_thread_safety(self):

        # Arrange
        def resolve_singleton():

            resolved_instance = DependencyResolver.resolve(ClassToBeResolved)

            time.sleep(0.1)

            return resolved_instance

        # Act
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

            futures = [executor.submit(resolve_singleton) for _ in range(10)]

            instances = [future.result() for future in concurrent.futures.as_completed(futures)]

        # Assert
        self.assertEqual(len(set(instances)), 1)


if __name__ == '__main__':
    print('Thread Safe Singleton Test')
    unittest.main()
