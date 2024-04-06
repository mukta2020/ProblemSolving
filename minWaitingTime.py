def minimumWaitingTime(queries):
    queries.sort()
    time = 0
    totalTime = 0
    for i in range(len(queries) - 1):
        time += queries[i]
        totalTime += time
    return totalTime

print( minimumWaitingTime([3,2,1,2,6]))