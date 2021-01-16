class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head = None

    def appendNode(self, value):
        if self.head == None: 
            self.head = Node(value)
            return

        current = self.head
        while (current.next != None):
            current = current.next

        current.next = Node(value)

    def printList(self):
        if self.head == None:
            return

        current = self.head
        while (current != None):
            print(current.value)
            current = current.next

        return


if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.appendNode(5)
    linked_list.appendNode(6)
    linked_list.appendNode(7)

    linked_list.printList()