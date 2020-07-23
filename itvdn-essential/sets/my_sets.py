import random as r

empty_set = set()
empty_frozen_set = frozenset()

empty_set = {1, 3, 4, 4, 5}
empty_frozen_set = frozenset([1, 3, 3, 2])
set_ = {x*2 for x in range(6)}
empty_set.add(434)
print(empty_set)
print(empty_frozen_set)
print(set_)

print(empty_set)