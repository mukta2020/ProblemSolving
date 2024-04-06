def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array)-1)

def shiftedBinarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right)//2
        pMatch = array[middle]
        leftNum = array[left]
        rightNum = array[right]
        if target == pMatch:
            return middle
        elif leftNum <= pMatch:
            if target< pMatch and target >= leftNum:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if target > pMatch and target <= rightNum:
                left = middle + 1
            else:
                right = middle - 1
    return -1