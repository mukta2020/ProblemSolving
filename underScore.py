def underscorifySubstring(string, substring):
    strList = string.split(" ")
    retStr = ""
    for str in strList:
        c = str.count(substring)
        if c > 0:
            c, lastCount, fstIdx, lastIdx = 0, 0, 0, 0
            idxList = []
            prelastIdx = 0
            entry = False
            for i in range(len(str)):
                if str[i: i + len(substring)] == substring:
                    if i <= prelastIdx and len(idxList) > 0:
                        fstIdx = idxList[-1][0]
                        idxList.pop(len(idxList)-1)
                        entry = False
                    if entry:
                        fstIdx = i
                        entry = False
                    lastIdx = i + len(substring)
                    c += 1
                elif lastCount != c:
                    idxList.append((fstIdx, lastIdx))
                    entry = True
                    lastCount, prelastIdx = c, lastIdx
                else:
                    fstIdx = i + 1

            if lastCount != c:
                    idxList.append((fstIdx, lastIdx))
            t = 0
            for i in range(len(idxList)):
                fstIdx = idxList[i][0] + t
                lastIdx = idxList[i][1] + t
                str = str[0: fstIdx] + "_" + str[fstIdx: lastIdx] + "_" + str[lastIdx:]
                t += 2
        retStr += str
        retStr += " "
    return retStr.strip(" ")
print(underscorifySubstring("tzttztttz", "ttt"))

#ttttttttttttttbtttttctatawtatttttastvb