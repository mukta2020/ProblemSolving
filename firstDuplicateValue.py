def firstDuplicateValue1(array):
    d = {}
    for i in range(len(array)):
        if array[i] not in d:
            d[array[i]] = 1
        else:
            return array[i]
    return -1
def firstDuplicateValue2(array):
    for i in range(len(array)):
        if array[i] in array[:i]:
            return array[i]
    return -1

def firstDuplicateValue3(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] == array[j]:
                return array[i]
    return -1
def firstDuplicateValue(array):
    for v in array:
        absVal = abs(v)
        index = absVal - 1
        if array[index] < 0:
            return absVal
        else:
            array[index] = array[index] * -1
    return -1

print(firstDuplicateValue([2,1,5,3,4,2]))