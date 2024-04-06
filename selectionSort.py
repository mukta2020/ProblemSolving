def selectionSort(array):
    """
    time limit exceed
    :param array:
    :return:
    """
    j = 0
    while j < len(array):
        min = array[j]
        minIdx = j
        for i in range(j, len(array)):
            if array[i] < min:
                min = array[i]
                minIdx = i
        array[j], array[minIdx] = array[minIdx], array[j]
        j += 1
    return array

print(selectionSort([8, 5, 2, 9, 5, 6, 3]))