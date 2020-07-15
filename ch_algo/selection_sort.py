def selection_sort(arr):
    start = 0
    while start < len(arr):
        for i in range(start, len(arr)):
            if arr[i] < arr[start]:
                arr[start], arr[i] = arr[i], arr[start]
        start += 1

l = [6, 8, 1, 4, 11, 8, 0, 21, 2, 5]
selection_sort(l)
print(l)