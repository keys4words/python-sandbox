def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        # print('bubble sort status: ' + str(arr))
        swap_happened = False
        for index in range(len(arr)-1):
            if arr[index] > arr[index+1]:
                swap_happened = True
                arr[index], arr[index+1] = arr[index+1], arr[index]

# l = [6, 8, 1, 4, 11, 8, 0, 21, 2, 5]
# bubble_sort(l)
# print(l)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# l = [6, 8, 1, 4, 11, 8, 0, 21, 2, 5]
# insertion_sort(l)
# print(l)

def selection_sort(arr):
    start = 0
    while start < len(arr):
        for i in range(start, len(arr)):
            if arr[i] < arr[start]:
                arr[start], arr[i] = arr[i], arr[start]
        start += 1

# l = [6, 8, 1, 4, 11, 8, 0, 21, 2, 5]
# selection_sort(l)
# print(l)

def merge(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr


def merging_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = merging_sort(arr[:middle])
        l2 = merging_sort(arr[middle:])
        return merge(l1, l2)


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for el in arr:
            if el < pivot:
                smaller.append(el)
            elif el == pivot:
                equal.append(el)
            else:
                larger.append(el)
            
    return quick_sort(smaller) + equal + quick_sort(larger)

# l = [6, 8, 1, 4, 11, 8, 0, 21, 2, 5]
# print(quick_sort(l))