def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    red, blue = 0, 0
    if redShirtHeights[0] > blueShirtHeights[0]:
        red = 1
    elif redShirtHeights[0] < blueShirtHeights[0]:
        blue = 1
    else:
        return False

    if red == 1:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
    elif blue == 1:
        for i in range(len(blueShirtHeights)):
            if blueShirtHeights[i] <= redShirtHeights[i]:
                return False
    return True