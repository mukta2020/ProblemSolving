
def update(array, i, largestArray):
    if largestArray[2] < array[i]:
        largestArray[2], largestArray[1], largestArray[0] = array[i], largestArray[2], largestArray[1]
    elif largestArray[1] < array[i] < largestArray[2]:
        largestArray[1], largestArray[0] = array[i], largestArray[1]
    elif array[i] <= largestArray[1] and largestArray[0] is None:
        largestArray[0] = array[i]
    elif largestArray[0] < array[i] < largestArray[1]:
        largestArray[0] = array[i]

def findThreeLargestNumbers(array):
    largestArray = [None, None, None]
    for i in range(0, len(array)):
        if largestArray[2] is None:
            largestArray[2] = array[i]
        elif largestArray[1] is None:
            if largestArray[2] >= array[i]:
                largestArray[1] = array[i]
            elif largestArray[2] < array[i]:
                largestArray[2], largestArray[1] = array[i], largestArray[2]
        else:
            update(array, i, largestArray)
    return largestArray

print(findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]))
#[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
