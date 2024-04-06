def isPalindrome(string):
    """
    T: O(n)  ; S: O(1)
    :param string:
    :return:
    """
    i, j = 0, len(string) - 1
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

def isPalindromeMy(string):
    return string == string[::-1]

def isPalindrome1(string):
    #T: O(n^2)  ; S: O(n)
    reverseString = ""
    for i in reversed(range(len(string))):
        reverseString += string[i]
    return string == reverseString

def isPalindrome3(string, i=0):
     j = len(string) -1 -i
     if i >= j:
         return True
     else:
        return string[i] == string[j] and isPalindrome3(string, i +1)
print(isPalindrome(''))