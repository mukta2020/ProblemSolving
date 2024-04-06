def numberOfWaysToTraverseGraph1(width, height):
    right = width - 1
    down = height - 1
    numerator = factorial(right + down)
    denominator = factorial(right) * factorial(down)
    return numerator // denominator

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
def numberOfWaysToTraverseGraph(width, height):
    traversmatrix =[[0 for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0:
                traversmatrix[i][j] = 1
            else:
                traversmatrix[i][j] = traversmatrix[i-1][j] + traversmatrix[i][j-1]
    return traversmatrix[height-1][width-1]

print(numberOfWaysToTraverseGraph(4,3))
