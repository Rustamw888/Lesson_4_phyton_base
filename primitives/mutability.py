# Списки, словари и множества - изменяемые!
from copy import deepcopy

l = [1, 2, 3, [4, 5, 6]]
ll = deepcopy(l)

ll[3].append(7)


d = {"key": "value", "some": {"first": 1}}
dd = deepcopy(d)

dd["some"]["second"] = 2


s = set()


# Кортежи, frozenset  - нет

t = (1, 2, 3, 4, 5)
tt = t

print()
