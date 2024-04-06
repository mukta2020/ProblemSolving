def spiralTraverse1(array):
    istRow, lstRow = 0, len(array) - 1
    istIndx = 0
    maxL = 0
    singleArr = []

    for i in range(len(array)):
        if len(array[i]) > maxL:
            maxL = len(array[i])
    maxL = maxL - 1

    while istRow <= lstRow and istIndx <= maxL:
       for i in range(istIndx, maxL + 1):
           singleArr.append(array[istRow][i])

       for j in range(istRow + 1, lstRow):
           rowMid = array[j]
           if len(rowMid) - 1 >= maxL:
               singleArr.append(rowMid[maxL])

       if istRow != lstRow:
           rowLast = array[lstRow]
           lstInd = len(rowLast) - 1
           if lstInd > maxL:
               lstInd = maxL
           for k in range(lstInd, istIndx - 1, -1):
               singleArr.append(rowLast[k])

       if istIndx != maxL:
           for l in range(lstRow - 1, istRow, -1):
               rowMid2 = array[l]
               if istIndx <= len(rowMid2):
                   singleArr.append(rowMid2[istIndx])
       istIndx += 1
       maxL -= 1
       istRow += 1
       lstRow -= 1
    return singleArr

def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append((array[startRow][col]))
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            result.append(array[endRow][col])
        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            result.append(array[row][startCol])
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result

a =  [ [1,2],
       [3,4,5],
       [6,7,8,9],
       [10,11]
  ]
print(spiralTraverse(a))
