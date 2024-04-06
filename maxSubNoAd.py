def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array

    maxSum = array[:]
    maxSum[0] = array[0]
    maxSum[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        maxSum[i] = max(maxSum[i-1], maxSum[i-2] + array[i])
    return maxSum[-1]


print(maxSubsetSumNoAdjacent([75,105,120,75,90,135]))