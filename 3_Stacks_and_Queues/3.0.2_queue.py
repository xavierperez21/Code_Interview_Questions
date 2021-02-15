class QueueNode:
    next = None
    data = 0
    def __init__(self, data):
        self.data = data


class MyQueue:
    first = None
    last = None

    def isEmpty(self):
        return self.first == None

    def peek(self):
        if (self.first == None): return None # Return an EmptyQueueException

        return self.first.data

    def add(self, item):
        node = QueueNode(item)
        if (self.last != None):
            self.last.next = node
        
        self.last = node

        if (self.first == None):
            self.first = self.last
        
    def remove(self):
        if (self.first == None): return None  # Return an EmptyQueueException
        
        node = self.first
        self.first = self.first.next
        
        if (self.first == None):
            self.last = None
        
        return node.data


if __name__ == "__main__":
    myQueue = MyQueue()
    
    myQueue.add(3)
    myQueue.add(12)
    myQueue.add(44)
    myQueue.add(8)

    print(myQueue.peek())
    print(myQueue.isEmpty())

    print(myQueue.remove())

    print(myQueue.peek())

    print(myQueue.remove())

    print(myQueue.peek())