def searchInSortedMatrix1(matrix, target):
    row, col = 0, 0
    num = matrix[row][col]
    while True:
        if row >= len(matrix):
            row -= 1
        if col >= len(matrix[0]):
            col -= 1
        if num < target:
            row += 1
            col += 1
            num = matrix[row][col]
        elif num > target:
            col -= 1
            n1 = matrix[row][col]
            while n1 >= target:
                if n1 > target:
                    col -= 1
                    n1 = matrix[row][col]
                elif n1 == target:
                    return [row, col]
            row -= 1
            n2 = matrix[row][col]
            while n2 >= target:
                if n2 > target:
                    row -= 1
                    n2 = matrix[row][col]
                elif n2 == target:
                    return [row, col]
        else:
            return [row, col]

def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row <= len(matrix) - 1 and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1,-1]


m = [[1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]]
print(searchInSortedMatrix(m, 3))
