def caesarCipherEncryptor1(string, key):
    d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
         10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r',
         19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
         }
    key_list = list(d.keys())
    val_List = list(d.values())
    retString = []
    for char in string:
        val = key_list[val_List.index(char)]
        newKey = val + key
        if newKey> 26:
           newKey = newKey % 26
        retString.append(d[newKey])
    return retString
def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    retString = ""
    for char in string:
        val = alphabet.index(char) + 1
        newKey = val + key
        if newKey > 26:
           newKey = newKey % 26
        retString += (alphabet[newKey-1])
    return retString
print(caesarCipherEncryptor("xyz", 2))