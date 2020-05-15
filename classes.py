from lazy_object import lazy_object
from timer import timer


class A:
    def __init__(self, num_elem):
        self.attr1 = list(range(num_elem))


a = lazy_object(A, num_elem=10 ** 8)

print(a)

with timer('Elapsed: {}ms'):
   type(a.attr1)

with timer('Elapsed: {}ms'):
   type(a.attr1)