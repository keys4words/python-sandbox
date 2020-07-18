values = [1, 3, 5, 4, 22, 911]
# print(values.__getitem__(1), values[1])
# print(values.__getitem__(slice(2,5)))
print(values)
del values[:2]
values.__delitem__(-1)
print(values)
# import collections.abc
# print(dir(collections.abc.MutableSequence))