def reverseWordsInString(string):
    retString = ""
    idx = len(string)
    wsfound = True
    i = 0
    for i in range(len(string)-1, -1, -1):
        if string[i] != " ":
            if not wsfound:
                idx = i + 1
            wsfound = True
        else:
            if wsfound:
                retString += string[i+1: idx] + " "
                idx = i
                wsfound = False
            else:
                retString += " "
    retString += string[i: idx]
    return retString
print(reverseWordsInString("test  "))
