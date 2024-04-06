def removeIslands(matrix):
    newMatrix = matrix[:]
    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    visited = [[False for c in range(col+1)] for r in range(row+1)]
    for r in range(row):
        for c in range(col):
            if r == 0 or c == 0 or r == row or c == col or visited[r][c]:
                visited[r][c] = True
                continue
            touchRecord, trueNeighbors = traverseNode(r, c, matrix, visited, newMatrix)
            if len(touchRecord) > 0 and True in touchRecord:
                continue
            newMatrix[r][c] = 0
            newMatrix = updateNewMatrix(trueNeighbors, newMatrix)
    return newMatrix
def updateNewMatrix(trueNeighbors, newMatrix):
    for neighbor in trueNeighbors:
        row = neighbor[0]
        col = neighbor[1]
        newMatrix[row][col] = 0
    return newMatrix

def traverseNode(row, col, matrix, visited, newMatrix):
    nodesToExplore = [[row, col]]
    touchRecord = []
    trueNeighbors = []
    while len(nodesToExplore):
        currNode = nodesToExplore.pop()
        row = currNode[0]
        col = currNode[1]
        if visited[row][col]:
            continue
        visited[row][col] = True
        if matrix[row][col] == 0:
            continue
        touch, unvisitedNeighbors = getUnvisitedNeighbours(row, col, visited, matrix)
        touchRecord.append(touch)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
            trueNeighbors.append(neighbor)
    return touchRecord, trueNeighbors

def getUnvisitedNeighbours(row, col, visited, matrix):
    unvisitedNeighbers = []
    touchBorder = False
    if row - 1 == 0 and matrix[0][col] == 1:
        touchBorder = True
        visited[0][col] = True
    if col - 1 == 0 and matrix[row][0] == 1:
        touchBorder = True
        visited[row][0] = True
    if row + 1 == len(matrix) - 1 and matrix[row + 1][col] == 1:
        touchBorder = True
        visited[row+1][col] = True
    if col + 1 == len(visited[0]) - 1 and matrix[row][col + 1] == 1:
        touchBorder = True
        visited[row][col + 1] = True

    if row > 0 and not visited[row - 1][col] and matrix[row - 1][col] != 0:
        unvisitedNeighbers.append([row-1, col])
    if row < len(visited) - 1 and not visited[row + 1][col] and matrix[row + 1][col] != 0:
        unvisitedNeighbers.append([row + 1, col])
    if col > 0 and not visited[row][col - 1] and matrix[row][col - 1] != 0:
        unvisitedNeighbers.append([row, col - 1])
    if col < len(visited[0]) - 1 and not visited[row][col + 1] and matrix[row][col + 1] != 0:
        unvisitedNeighbers.append([row, col + 1])
    return touchBorder, unvisitedNeighbers

matrix = [[1,0,0,0,0,0],[0,1,0,1,1,1], [0,0,1,0, 1, 0], [1,1,0,0,1,0], [1,0,1,1,0,0],[1,0,0,0,0,1]]

print(removeIslands(matrix))
