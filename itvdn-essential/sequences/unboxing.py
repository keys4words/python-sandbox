def mean(first, *numbers):
    sum_ = first + sum(numbers)
    return sum_/(len(numbers)+1)

print(mean(1, 3, 5))
values = [4, 5, 7, 8]
print(*values)