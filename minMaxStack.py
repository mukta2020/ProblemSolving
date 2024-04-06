
class MinMaxStack:
    def __init__(self):
        self.minMaxStack = [0, 0]
        self.stack = []
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]

    def pop(self):
        if len(self.stack) >= 1:
            p = self.stack.pop()
            if len(self.stack) >= 1:
                min_value = min(self.stack)
                max_value = max(self.stack)
                self.minMaxStack[0] = min_value
                self.minMaxStack[1] = max_value
            else:
                self.minMaxStack[0] = 0
                self.minMaxStack[1] = 0
            return p

    def push(self, number):
        self.stack.append(number)
        min_value = min(self.stack)
        max_value = max(self.stack)
        self.minMaxStack[0] = min_value
        self.minMaxStack[1] = max_value

    def getMin(self):
        if len(self.minMaxStack) > 0:
            return self.minMaxStack[0]

    def getMax(self):
        if len(self.minMaxStack) > 0:
            return self.minMaxStack[1]

m = MinMaxStack()
m.push(2)
m.push(0)
m.push(5)
m.push(4)
print(m.getMax())
print(m.getMin())
print(".....pop........")
print(m.pop())
print(m.pop())
print("........pop end........")
m.push(4)
m.push(11)
print(m.pop())
print(m.pop())
print(m.pop())
print(m.pop())

print(m.pop())
m.push(6)
print(m.pop())