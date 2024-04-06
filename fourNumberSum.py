def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruples = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            diff = targetSum - currentSum
            if diff in allPairSums:
                for pair in allPairSums[diff]:
                    quadruples.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruples
print(fourNumberSum([5,-5,-2,2,3,-3], 0))