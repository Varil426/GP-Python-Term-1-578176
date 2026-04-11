class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
            # last = self.stack[-1]
            # del self.stack[-1]
            # return last

    def peek(self):
        if not self.is_empty():
            # last_index = self.size() - 1
            # return self.stack[last_index]
            return self.stack[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)


# Testy
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())  # 3
    print(stack.peek())  # 2
    print(stack.is_empty())  # False
    print(stack.size())  # 2
