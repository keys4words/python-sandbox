def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        print('bubble sort status: ' + str(arr))
        swap_happened = False
        for index in range(len(arr)-1):
            if arr[index] > arr[index+1]:
                swap_happened = True
                arr[index], arr[index+1] = arr[index+1], arr[index]

l = [6, 8, 1, 4, 11, 8, 0, 21, 2, 5]
bubble_sort(l)
print(l)