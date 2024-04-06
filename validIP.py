
def validIPAddresses1(string):
    l = len(string)
    validIPs = []
    if 4 <= l <= 12:
        first, second, thirth, fourth, = 0,0,0,0
        if l == 4:
            ip = string[0] + "." + string[1] + "." + string[2] + "." + string[3]
            validIPs.append(ip)
        elif l == 5:
            if string[3] != "0":
                ip = string[0] + "." + string[1] + "." + string[2] + "." + string[3:4]
                validIPs.append(ip)
            if string[2] != "0":
                ip = string[0] + "." + string[1] + "." + string[2:3] + "." + string[4]
                validIPs.append(ip)
            if string[1] != "0":
                ip = string[0] + "." + string[1:2] + "." + string[3] + "." + string[4]
                validIPs.append(ip)
            if string[0] != "0":
                ip = string[0:1] + "." + string[2] + "." + string[3] + "." + string[4]
                validIPs.append(ip)
        elif l == 6:
            if string[3] != "0" and int(string[3:5]) <= 255:
                ip = string[0] + "." + string[1] + "." + string[2] + "." + string[3:5]
                validIPs.append(ip)
            if string[2] != "0":
                ip = string[0] + "." + string[1] + "." + string[2:3] + "." + string[4]
                validIPs.append(ip)
            if string[1] != "0":
                ip = string[0] + "." + string[1:2] + "." + string[3] + "." + string[4]
                validIPs.append(ip)
            if string[0] != "0":
                ip = string[0:1] + "." + string[2] + "." + string[3] + "." + string[4]
                validIPs.append(ip)

    return validIPs

def validIPAddresses(string):
    ipFound = []
    for i in range(1, min(len(string), 4)):
        currIP = ["","","",""]
        currIP[0] = string[:i]
        if not isValidPart(currIP[0]):
            continue
        for j in range(i + 1, i + min(len(string)- i, 4)):
            currIP[1] = string[i:j]
            if not isValidPart(currIP[1]):
                continue
            for k in range(j + 1, j + min(len(string) - j, 4)):
                currIP[2] = string[j:k]
                currIP[3] = string[k:]
                if isValidPart(currIP[2]) and isValidPart(currIP[3]) :
                    ipFound.append(".".join(currIP))
    return ipFound

def isValidPart(string):
    intString = int(string)
    if intString > 255:
        return False
    return len(str(intString)) == len(string)

print(validIPAddresses("1921680"))

