def longestCommonSubsequence(str1, str2):
    m = len(str1) # row
    n = len(str2)  # col
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    b = [['*' for i in range(1, n+1)] for j in range(1, m+1)]

    for i in range(0, m):
        for j in range(0, n):
            if str1[i] == str2[j]:
                #c[i][j] = c[i-1][j-1] + 1
                c[i+1][j+1] = c[i][j] + 1
                b[i][j] = 'd'
            elif c[i][j+1] >= c[i+1][j]:
                #c[i][j] = c[i-1][j]
                c[i+1][j+1] = c[i][j+1]
                b[i][j] = 'u'
            else:
                #c[i][j] = c[i][j-1]
                c[i+1][j+1] = c[i+1][j]
                b[i][j] = 'h'

    lcs = []
    lcs = printLCS(b, str1, len(str1) - 1, len(str2) - 1, lcs)
    return [] if lcs is None else lcs


def printLCS(b, str1, i, j, lcs):
    if i < 0 or j < 0:
        return
    if b[i][j] == 'd':
        lcs.append(str1[i])
        printLCS(b, str1, i-1, j-1, lcs)
    elif b[i][j] == 'u':
        printLCS(b, str1, i-1, j, lcs)
    else:
        printLCS(b, str1, i, j-1, lcs)
    return lcs[::-1]

X = ''
Y = ''
print(longestCommonSubsequence(X, Y))
