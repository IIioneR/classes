from lazy_object import lazy_object
from timer import timer


class A:
    def __init__(self, num_elem):
        self.reset = 0
        self.attr1 = list(range(num_elem))


a = lazy_object(A, num_elem=10 ** 5)

print(a)  # 0.006

with timer('Elapsed: {}ms'):
    type(a.attr1)  # 0.006

with timer('Elapsed: {}ms'):
    type(a.attr1)  # 0.003

a.reset = 1

with timer('Elapsed: {}ms'):
    type(a.attr1)  # 0.006

with timer('Elapsed: {}ms'):
    type(a.attr1)  # 0.003
