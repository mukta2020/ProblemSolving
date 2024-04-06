def checkCity(distances, fuel, idx):
    distances = distances[idx:] + distances[:idx]
    fuel = fuel[idx:] + fuel[:idx]

    distance = fuel[0]
    for i in range(0, len(fuel) - 1):
        distance -= distances[i]
        if distance >= 0:
            distance += fuel[i + 1]
        else:
            return False
    return True

def validStartingCity(distances, fuel, mpg):

    for j in range(len(fuel)):
        fuel[j] = fuel[j] * mpg

    for i in range(len(distances)):
        if not checkCity(distances, fuel, i):
            continue
        else:
            return i
    return -1
print(validStartingCity([30, 40, 10, 10, 17, 13, 50, 30, 10, 40], [1, 2, 0, 1, 1, 0, 3, 1, 0, 1],25))