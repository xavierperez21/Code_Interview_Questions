class MyStack:
    top = None

    def isEmpty(self):
        return self.top == None

    def peek(self):
        if (self.top == None): return None  # Return an exception
        return self.top.data

    def push(self, item):
        node = StackNode(item)
        node.next = self.top
        self.top = node

    def pop(self):
        if (self.top == None): return None # Return an exception
        node = self.top
        self.top = self.top.next
        return node.data


class StackNode:
    data = 0
    next = None
    def __init__(self, data):
        self.data = data


if __name__ == "__main__":
    myStack = MyStack()
    myStack.push(9)
    myStack.push(22)
    myStack.push(1)

    print(myStack.peek())

    print(myStack.pop())

    print(myStack.isEmpty())

    print(myStack.peek())