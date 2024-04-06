def longestSubstringWithoutDuplication1(string):
    d = {}
    curSubStr, lSubStr = "", ""
    preIndex, maxLength = 0, 0
    for i in range(0, len(string)):
        if string[i] not in curSubStr:
            d[string[i]] = i
            curSubStr += string[i]
        else:
            curLength = i - preIndex
            if curLength > maxLength:
                maxLength = curLength
                lSubStr = curSubStr
            preIndex = d[string[i]] + 1
            d[string[i]] = i
            curSubStr = string[preIndex: i + 1]
    if len(curSubStr) > len(lSubStr):
        return curSubStr
    else:
        return lSubStr

#print(longestSubstringWithoutDuplication1("clementisacap"))


def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < i+1 - startIdx:
            longest = [startIdx, i+1]
        lastSeen[char] = i
    return string[longest[0]: longest[1]]
print(longestSubstringWithoutDuplication("clementisacap"))
