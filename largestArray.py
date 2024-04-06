def largestRange(array):
    array.sort()
    low = array[0]
    count = 1
    largeRange = [low, array[0]]
    for i in range(1, len(array)):
        if array[i] == array[i - 1] + 1 or array[i] == array[i - 1]:
            count += 1
        else:
            if count > largeRange[1] - largeRange[0]:
                largeRange[0] = low
                largeRange[1] = array[i-1]
            low = array[i]
            count = 1
    if count > largeRange[1] - largeRange[0]:
        largeRange[0] = low
        largeRange[1] = array[-1]
    return largeRange

print(largestRange([0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]))