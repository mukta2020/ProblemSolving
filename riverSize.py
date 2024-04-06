def riverSizes(matrix):
    sizes = []
    row = len(matrix)
    col = len(matrix[0])
    visited = [[False for c in range(col)] for r in range(row)]
    for r in range(row):
        for c in range(col):
            if visited[r][c]:
                continue
            traverseNode(r, c, matrix, visited, sizes)
    return sizes
def traverseNode(row, col, matrix, visited, sizes):
    currSize = 0
    nodesToExplore = [[row, col]]
    while len(nodesToExplore):
        currNode = nodesToExplore.pop()
        row = currNode[0]
        col = currNode[1]
        if visited[row][col]:
            continue
        visited[row][col] = True
        if matrix[row][col] == 0:
            continue
        currSize += 1
        unvisitedNeighbors = getUnvisitedNeighbours(row, col, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currSize > 0:
        sizes.append(currSize)
    return

def getUnvisitedNeighbours(row, col, visited):
    unvisitedNeighbers = []
    if row > 0 and not visited[row - 1][col]:
        unvisitedNeighbers.append([row-1, col])
    if row < len(visited) - 1 and not visited[row + 1][col]:
        unvisitedNeighbers.append([row + 1, col])
    if col > 0 and not visited[row][col - 1]:
        unvisitedNeighbers.append([row, col - 1])
    if col < len(visited[0]) - 1 and not visited[row][col + 1]:
        unvisitedNeighbers.append([row, col + 1])
    return unvisitedNeighbers

matrix = [[1,0,0],[1,0,1]]
print(riverSizes(matrix))
