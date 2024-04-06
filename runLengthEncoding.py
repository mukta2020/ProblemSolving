def runLengthEncoding(string):
    count = 1
    finalString = ""
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            count += 1
            if count > 9:
                finalString += str(count - 1) + string[i - 1]
                count = 1
        else:
            finalString += str(count) + string[i - 1]
            count = 1
    return finalString + str(count) + string[len(string)-1]
print(runLengthEncoding(" "))

