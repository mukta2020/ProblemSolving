def sortedSquaredArray1(array):
    for i in range(len(array)):
        array[i] = array[i] * array[i]
    return sorted(array)

def sortedSquaredArray(array):
    new_array = [0 for _ in array]
    Idxlow = 0
    Idxhigh = len(array) -1

    for i in reversed(range(len(array))):
        low = array[Idxlow]
        high = array[Idxhigh]
        if abs(array[Idxlow]) > abs(array[Idxhigh]):
            new_array[i] = low * low
            Idxlow += 1
        else:
            new_array[i] = high * high
            Idxhigh -= 1
    return new_array
print(sortedSquaredArray([-1, -2 , -3, -4]))

