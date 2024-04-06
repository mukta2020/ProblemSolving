def isMonotonic(array):
    if len(array) <= 1:
        return True
    minFlag, maxFlag = True, True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            maxFlag = False
        if array[i] > array[i - 1]:
            minFlag = False
    return minFlag or maxFlag


def checkDecrising(array):
    min = array[0]
    for i in range(1, len(array)):
        if array[i] <= min:
            min = array[i]
        else:
            return False
    return True
def checkIncreasing(array):
    max = array[0]
    for i in range(1, len(array)):
        if array[i] >= max:
            max = array[i]
        else:
            return False
    return True

def isMonotonic1(array):
    if len(array) > 1:
        return checkDecrising(array) or checkIncreasing(array)
    else:
        return True

print(isMonotonic([1,2]))