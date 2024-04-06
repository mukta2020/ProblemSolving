
def staircaseTraversal(height, maxSteps, total):
    for step in range(1, maxSteps+1):
        if step == 1:
            total = 1
        elif step == height:
            total += 1
        else:
            total += recursivehelper(height, step, total)
    return total

def recursivehelper(height, step, total):
    stepfreq = 1
    stepfrequencies = [stepfreq]
    uniquefreq = height - (stepfreq * step)
    while uniquefreq >= 0:
        total = helper(uniquefreq, stepfrequencies, total, step, stepfreq, height)
        stepfreq += 1
        stepfrequencies = [stepfreq]
        uniquefreq = height - stepfreq * step
    return total

def helper(uniquefreq, stepfrequencies, total, step, stepfreq, height ):
    if uniquefreq == 0:
        total += 1
        return total
    total = calculate(uniquefreq, stepfrequencies, total)
    if step > stepfreq * step - 1 > 1:
        newfreq = 1
        newStep = stepfreq * step - 1
        newuniquefreq = height - (stepfreq * step + newfreq * newStep)
        stepfrequencies.append(newfreq)
        total += helper(newuniquefreq, stepfrequencies, total, step, stepfreq, height)
        
    return total


def calculate(uniquefreq, stepfrequencies, total):
    totalfeq = 0
    d = 1
    for stepfreq in stepfrequencies:
        totalfeq += stepfreq
        d *= factorial(stepfreq)
    numerator = factorial(uniquefreq + totalfeq)
    denominator = d * factorial(uniquefreq)
    total += numerator // denominator
    return total
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(staircaseTraversal(6, 3, 0))