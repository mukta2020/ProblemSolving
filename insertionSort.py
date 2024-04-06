def insertionSort1(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#card insertion example
def insertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        while j >= 0 and array[j + 1] < array[j]:
            array[j + 1], array[j] = array[j], array[j + 1]
            j -= 1
    return array

arr = [12, 11, 13, 5, 6]
print(insertionSort(arr))