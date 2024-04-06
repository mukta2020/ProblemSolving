def knapsackProblem(items, capacity):
    rows, cols = (len(items) + 1, capacity + 1)
    bag = []
    v = [[0 for i in range(cols)] for j in range(rows)]
    # # v[0][5] = 5
    # for row in v:
    #     print(row)
    for j in range(1, cols):
        for i in range(1, rows):
            w = items[i-1][1]
            val = items[i-1][0]
            if w <= j:
                v[i][j] = max(v[i-1][j], v[i-1][j-w] + val)
            else:
                v[i][j] = v[i-1][j]
    # for row in v:
    #     print(row)
    i, j = rows - 1, cols - 1
    totalItem = 0
    idx = []
    while i != 0:
        if v[i][j] != v[i - 1][j]:
            #bag.append(items[i - 1])
            totalItem += items[i - 1][0]
            idx.append(i - 1)
            j = j - items[i - 1][1]
        i = i - 1
    bag.append(totalItem)
    bag.append(list(reversed(idx)))
    return bag

print(knapsackProblem([[1,2], [4,3], [5,6], [6,7]], 10))
