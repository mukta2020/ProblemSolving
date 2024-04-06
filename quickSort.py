def quick_swap_udacity(nums, low, high):
    pivot = nums[high]
    while (low < high):
        while (nums[low] > pivot):
            nums[low], nums[high - 1] = nums[high - 1], nums[low]
            nums[high], nums[high - 1] = nums[high - 1], nums[high]
            high -= 1
        low += 1
    return high
def quickhelper_udacity(arr, low, high):
    if low < high:
        pi = quick_swap_udacity(arr, low, high)
        quickhelper_udacity(arr, low, pi - 1)
        quickhelper_udacity(arr, pi + 1, high)

def partition(arr, low, high):
    """
    Runtime: 240 ms, faster than 76.62% of Python online submissions for Sort an Array.
Memory Usage: 19.1 MB, less than 60.89% of Python online submissions for Sort an Array.
    """
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSorthelper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSorthelper(arr, low, pi - 1)
        quickSorthelper(arr, pi + 1, high)

def quickSort(array):
    quickhelper_udacity(array, 0, len(array) - 1)
    return array
#arr = [10, 7, 8, 9, 1, 5]
arr = [5,2,3,1]
print(quickSort(arr))
