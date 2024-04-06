def minNumberOfJumps(array):
    jumps, i = 0, 0
    curVal = array[0]
    curIdx = 0
    while curIdx + curVal < len(array) - 1:
        maxVal = -float("inf")
        count = 0
        for i in range(curIdx + 1, curIdx + 1 + curVal):
            if array[i] >= maxVal:
                maxVal = array[i]
                curIdx = i
                count = 0
            else:
                count += 1
        if count == maxVal:
            maxVal = array[i]
            curIdx = i
        curVal = maxVal
        jumps += 1
    if curIdx < len(array) - 1:
        return jumps + 1
    else:
        return jumps
print(minNumberOfJumps([3, 12, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]))
#[2, 1, 2, 2, 1, 1, 1]
#[3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]