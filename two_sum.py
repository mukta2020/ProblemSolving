def twoNumberSum(array, targetSum):
    h = {}
    i = 0
    for num1 in array:
        num2 = targetSum - num1
        if num2 in h:
            return [num1, num2]
        h[num1] = i
        i += 1
    return []
def twoNumberSum2(array, targetSum):
    h = {}
    for num1 in array:
        num2 = targetSum - num1
        if num2 in h:
            return [num1, num2]
        h[num1] = True
    return []
def twoNumberSum3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
print(twoNumberSum3([2, 7, 11, 15], 9))