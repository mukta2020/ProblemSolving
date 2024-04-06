def validStartingCity(distances, fuel, mpg):
    for j in range(len(fuel)):
        fuel[j] = fuel[j] * mpg
    milesLeft = 0
    minGas = 0
    minCity = 0

    for i in range(len(distances)):
        milesLeft += (fuel[i] - distances[i])
        if milesLeft < minGas:
            minGas = milesLeft
            minCity = i+1
    return minCity
print(validStartingCity([5,25,15,10,15],[1,2,1,0,3],10))