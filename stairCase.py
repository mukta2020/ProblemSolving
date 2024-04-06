def staircaseTraversalMe(height, maxSteps):
    stair = [0 for i in range(height+1)]
    stair[0] = 1
    stair[1] = 1
    for i in range(2, height + 1):
        endwindow = i
        startWindow = endwindow - maxSteps
        if startWindow < 0:
            startWindow = 0
        stair[i] = sum(stair[startWindow: endwindow])
    return stair[height]

def staircaseTraversal3(height, maxSteps):
    stair = [0 for i in range(height+1)]
    stair[0] = 1
    stair[1] = 1

    for currentHight in range(2, height+1):
        step = 1
        while step <= maxSteps and step <= currentHight:
            stair[currentHight] = stair[currentHight] + stair[currentHight-step]
            step += 1
    return stair[height]

def staircaseTraversal1(height, maxSteps):
    if height <= 1:
        return 1
    noOfways = 0
    for step in range(1, min(maxSteps, height)+1):
        noOfways += staircaseTraversal1(height-step, maxSteps)
    return noOfways

def staircaseTraversal2(height, maxSteps):
    return staircaseTraversalMemoize(height,maxSteps, {0:1, 1:1})
def staircaseTraversalMemoize(height, maxSteps, memo):
    if height in memo:
        return memo[height]
    noOfways = 0
    for step in range(1, min(maxSteps, height)+1):
        noOfways += staircaseTraversalMemoize(height-step, maxSteps, memo)
    memo[height] = noOfways
    return noOfways

def staircaseTraversal(height, maxSteps):
    noOfways = 0
    stair = [1]
    for currHeight in range(1, height +1):
        startWindow = currHeight - maxSteps - 1
        endWindow = currHeight - 1
        if startWindow >= 0:
            noOfways -= stair[startWindow]
        noOfways += stair[endWindow]
        stair.append(noOfways)
    return stair[height]

print(staircaseTraversalMe(4,3))

