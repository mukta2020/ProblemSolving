def balancedBrackets(string):
    stack = []
    mapping = {")": "(",    "}": "{",         "]": "["}
    openningBrackets = "([{"
    closingBrackets = ")]}"
    for char in string:
        if char in openningBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(balancedBrackets("("))