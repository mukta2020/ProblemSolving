def threeNumberSort1(array, order):
    valueCounts = [0,0,0]
    for el in array:
        orderIdx = order.index(el)
        valueCounts[orderIdx] += 1
    for i in range(3):
        value = order[i]
        count = valueCounts[i]

        numElBefore = sum(valueCounts[:i])
        for n in range(count):
            currIdx = numElBefore + n
            array[currIdx] = value
    return array
def threeNumberSort(array, order):
    firstValue = order[0]
    thirdValue = order[2]

    firstIdx = 0
    for i in range(len(array)):
        if array[i] == firstValue:
            array[firstIdx], array[i] = array[i],  array[firstIdx]
            firstIdx += 1
    thirdIdx = len(array) - 1
    for i in range(len(array) - 1, -1, -1):
        if array[i] == thirdValue:
            array[thirdIdx], array[i] = array[i], array[thirdIdx]
            thirdIdx -= 1

    return array


print(threeNumberSort([1,0,0,-1,-1,0,1,1], [0,1,-1]))
