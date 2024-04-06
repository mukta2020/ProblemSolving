def taskAssignment(k, tasks):
    taskArray = []
    for i in range(k):
        low, high = float('inf'), float('-inf')
        idx1, idx2 = -1, -1
        for j in range(len(tasks)):
            if tasks[j] == "D":
                continue
            if tasks[j] < low:
                low = tasks[j]
                idx1 = j
            if tasks[j] >= high:
                high = tasks[j]
                idx2 = j
        tasks[idx1] = "D"
        tasks[idx2] = "D"
        taskArray.append([idx1, idx2])
    return taskArray
print(taskAssignment(3, [1,3,5,3,1,4]))