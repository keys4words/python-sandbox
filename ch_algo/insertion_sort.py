def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

l = [6, 8, 1, 4, 11, 8, 0, 21, 2, 5]
insertion_sort(l)
print(l)