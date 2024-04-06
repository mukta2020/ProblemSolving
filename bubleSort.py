def bubbleSort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
    return array
#scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
scores =  [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(scores))