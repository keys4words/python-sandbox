from functools import reduce

values = [2, 4, 1, 7, 0, 55]
# mapping
# result = list(map(lambda x: x**2, values))
# print(result)

# filtering
# result = list(filter(lambda x: x%2==0, values))
# print(result)

# reducing
result = reduce(lambda x, y: x + y , values)
print(result, sum(values))