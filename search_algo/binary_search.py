def bisection_iter(n, arr):
    start = 0
    stop = len(arr) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return f"{n} found at index: {mid}"
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    print('start=', start)
    print('stop=', stop)
    return f"{n} not found in list"

def create_list(max_val):
    arr = []
    for num in range(1, max_val+1):
        arr.append(num)
    return arr


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#inx 0  1  2  3  4  5  6  7  8  9

num_to_search = -1
print(bisection_iter(num_to_search, l))
