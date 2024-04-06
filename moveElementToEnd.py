def moveElementToEnd(array, toMove):
    i, moveIdx = 0, 0
    while i < len(array) and moveIdx < len(array):
        if array[i] != toMove and array[moveIdx] == toMove:
            array[i], array[moveIdx] = array[moveIdx], array[i]
        if array[moveIdx] != toMove:
            moveIdx += 1
        i += 1
    return array
print(moveElementToEnd([2,2,1,4,2], 2))