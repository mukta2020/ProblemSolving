def subarraySort(array):
    lowIdx, highIdx = 0, 0
    orderedLast = array[0]
    unorderdMax = array[0]
    unorderFound = False
    subarray = [lowIdx, highIdx]
    for i in range(1, len(array)):
        if unorderFound and array[i] > unorderdMax:
            subarray[0] = lowIdx
            subarray[1] = highIdx
        if array[i] > array[i-1]:
            unorderFound = False
            orderedLast = array[i]
            lowIdx = i
        else:
            unorderFound = True
            unorderdMax = array[i-1]
            highIdx = i
            j = i
            while array[i] <= array[j-1]:
                j -= 1
            lowIdx = j
    return subarray

print(subarraySort([1,2,4,7,10,11,7,12,6,7,16,18,19]))