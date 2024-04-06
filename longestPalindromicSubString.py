def isPalindrome(string):
    i, j = 0, len(string) - 1
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

def longestPalindromicSubstring(string):
    longString = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            subStr= string[i: j+1]
            if len(subStr) > len(longString) and isPalindrome(subStr):
                longString = subStr
    return longString

print(longestPalindromicSubstring("abcxyyxf"))