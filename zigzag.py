def zigzagTraverse(array):
    d = {}
    res = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i + j not in d:
                d[i + j] = [array[i][j]]
            else:
                d[i + j].append(array[i][j])
    for k, v in d.items():
        if k % 2 != 0:
            res.extend((v[::-1]))
        else:
            res.extend(v)
    return res


def zigzagTraverse1(array):
    if not array:
        return array
    rows, cols = len(array), len(array[0])
    new_rows = rows + cols - 1  # one-dimentional matrix
    result = []
    A = [[] for i in range(new_rows)]

    for r in range(rows):
        for c in range(cols):
            A[r + c].append(array[r][c])

    for i in range(new_rows):
        if i % 2 != 0:
            A[i].reverse()
        result += A[i]
    return result

a = [  [1,3,4,10],
       [2,5,9,11],
       [6,8,12,15],
       [7,13,14,16]
     ]
print(zigzagTraverse1(a))

def findDiagonalOrder(matrix):
        """
        Runtime: 164 ms, faster than 87.31% of Python online submissions for Diagonal Traverse.
        Memory Usage: 16.7 MB, less than 41.09% of Python online submissions for Diagonal Traverse.
        https://leetcode.com/problems/diagonal-traverse/submissions/
        :param matrix:
        :return:
        """
        if not matrix:
            return matrix
        rows, cols = len(matrix), len(matrix[0])
        new_rows = rows + cols - 1  # one-dimentional matrix
        result = []
        A = [[] for i in range(new_rows)]

        for r in range(rows):  # Step1: generate A. numbers in same diagonal have same value of row+col
            for c in range(cols):
                A[r + c].append(matrix[r][c])

        for i in range(new_rows):  # Step2: reverse numbers in even diagonals.
            if i % 2 == 0:
                A[i].reverse()
            result += A[i]
        return result