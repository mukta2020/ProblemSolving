def Pattern_Position_List(pattern):
    """
    "xxy"
    {"x": [0, 1], "y": [2]}
    """
    d = {}
    for i, char in enumerate(pattern):
        if char not in d:
            d[char] = [i]
        else:
            d[char].append(i)
    return d
def getNewPattern(pattern):
    pList = list(pattern)
    if pattern[0] == "x":
        return pList
    else:
        return list(map(lambda char: "x" if char == "y" else "y", pList))

def patternMatcher(pattern, string):
    pSet = set(pattern)
    strSet = set(string)
    output = []
    if len(pSet) == 1:
        t = int((len(string) / len(pattern)))
        if pattern.count("x") > 0:
            return [string[0: t], ""]
        else:
            return ["", string[0: t]]
    elif len(pattern) == len(string) and len(pSet) == len(strSet) == 2:
            xPos = pattern.find("x")
            yPos = pattern.find("y")
            output.append(string[xPos])
            output.append(string[yPos])
    else:
        newPattern = getNewPattern(pattern)
        match = newPattern[0] == pattern[0]
        dct = Pattern_Position_List(newPattern) # {"x": [0,1], "y": [2]}
        yPosInPtn = dct["y"][0]
        noOfX = len(dct["x"])
        noOfY = len(dct["y"])
        lnX = 1
        while lnX < len(string):
            lnY = int((len(string) - lnX * noOfX)/noOfY)
            if lnY % 1 != 0:
                continue
            yIdx = yPosInPtn * lnX
            x = string[:lnX]
            y = string[yIdx: yIdx + lnY]
            potentialMatch = map(lambda char: x if char == "x" else y, newPattern)
            pMatchString = "".join(potentialMatch)
            if string == pMatchString:
                if not match:
                    x, y = y, x
                output.append(x)
                output.append(y)
                return output
            else:
                lnX += 1
    return output

print(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"))

