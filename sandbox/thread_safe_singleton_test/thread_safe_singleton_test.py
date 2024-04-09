import concurrent.futures
import time
import unittest
from pinjet.core.resolver.dependency_resolver import DependencyResolver
from pinjet.core.annotations.injectable import injectable


@injectable
class ClassToBeResolved:
    pass


class TestSingletonResolverThreadSafety(unittest.TestCase):

    def test_singleton_thread_safety(self):

        def resolve_singleton(worker_id: int):

            print(f'worker {worker_id}')

            resolved_instance = DependencyResolver.resolve(ClassToBeResolved)

            print(f'resolved instance: {resolved_instance} by worker {worker_id}')

            time.sleep(0.1)

            return resolved_instance

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

            futures = [executor.submit(resolve_singleton, _) for _ in range(10)]

            instances = [future.result() for future in concurrent.futures.as_completed(futures)]

        self.assertEqual(len(set(instances)), 1)


if __name__ == '__main__':
    unittest.main()
