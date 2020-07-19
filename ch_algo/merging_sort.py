def merging(arr1, arr2):
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

l1 = [1, 4, 6, 8, 10]
l2 = [2, 3, 5, 7, 8, 9]
print(f"merging list: {merging(l1, l2)}")