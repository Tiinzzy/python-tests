class StackImpl:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        removed = self.stack.pop()
        return removed

    def isEmpty(self):
        print(self.size == 0)
    
    def size(self):
        print(len(self.stack))

    def peek(self):
        print(self.stack[-1])

    def print(self):
        print(self.stack)