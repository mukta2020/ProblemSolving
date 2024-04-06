def quickselect(array, k):
    array.sort()
    return array[k-1]
print(quickselect([8,5,2,9,7,6,3], 3))