
def kadanesAlgorithm(array):
    maxSum, curSum = array[0], array[0]

    for i in range(1, len(array)):
        curSum += array[i]
        if curSum < array[i]:
            curSum = array[i]
        maxSum = max(curSum, maxSum)
    return max(curSum, maxSum)

