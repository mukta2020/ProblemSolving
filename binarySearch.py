def binarySearch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            high = mid - 1
        elif target > array[mid]:
            low = mid + 1
    return -1
print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))