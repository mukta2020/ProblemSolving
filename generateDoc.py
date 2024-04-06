def generateDocument(characters, document):

    charDict = {}
    docDict = {}
    for char in characters:
        if char not in charDict:
            charDict[char] = 1
        else:
            charDict[char] += 1
    for char in document:
        if char not in docDict:
            docDict[char] = 1
        else:
            docDict[char] += 1
    if charDict == docDict:
        return True
    else:
        for k1, v1 in docDict.items():
            if k1 not in charDict:
                return False
            if charDict[k1] < docDict[k1]:
                return False
        return True
print(generateDocument("abcabc", "aabbccc"))