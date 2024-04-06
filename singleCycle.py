def hasSingleCycle(array):
    l = len(array) -1
    idx = 0
    while l >= 0:
        if abs(idx) > len(array) - 1:
            idx = idx % len(array)
        if array[idx] == "V":
            return False
        value = array[idx]
        if idx == len(array) - 1:
            idx = array[idx]-1
            array[len(array) - 1] = "V"
        else:
            array[idx] = "V"
            idx += value
        l -= 1
    if abs(idx) > len(array) - 1:
        idx = idx % len(array)
    return True if idx == 0 else False

print(hasSingleCycle([1,2,3,4,-2,3,7,8,-26]))