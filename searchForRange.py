def searchForRange(array, target):
    finalRange = [-1, -1]
    searchForRangeHelper(array, target, 0, len(array) -1, finalRange, True)
    searchForRangeHelper(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange
def searchForRangeHelper(array, target, left, right, finalRange, goLeft):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid -1
        else:
            if goLeft:
                if mid == 0 or array[mid -1] != target:
                    finalRange[0] = mid
                    return
                else:
                    right = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return
                else:
                    left = mid + 1

print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73],45))