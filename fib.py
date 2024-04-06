def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)

def productSumHelper(array, depth):
    sum = 0
    for i in range(0, len(array)):
        if type(array[i]) == list:
            sum += productSumHelper(array[i], depth +1)
        elif type(array[i]) == int:
            sum += array[i]
    return sum * depth

def productSum(array):
    sum = 0
    depth = 1
    return productSumHelper(array, depth)



print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
