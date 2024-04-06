def sunsetViews(buildings, direction):
    indices = []
    if len(buildings) > 0:
        lastmaxBuilding = buildings[0]
        if direction == "EAST":
            indices.append(len(buildings)-1)
            lastmaxBuilding = buildings[len(buildings)-1]
            for i in range(len(buildings)-1, -1, -1):
                if buildings[i] > lastmaxBuilding:
                    indices.append(i)
                    lastmaxBuilding = buildings[i]
            indices = indices[::-1]
        else:
            indices.append(0)
            for i in range(len(buildings)):
                if buildings[i] > lastmaxBuilding:
                    indices.append(i)
                    lastmaxBuilding = buildings[i]
    return indices


print(sunsetViews([], "WEST"))