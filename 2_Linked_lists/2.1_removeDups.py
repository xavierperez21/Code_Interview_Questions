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

        array = list()
        current = self.head
        while (current != None):
            array.append(current.value)
            current = current.next

        print(array)
        return

    # Before the head node
    def prependNode(self, value):
        if (self.head == None):
            self.head = Node(value)
            return
        
        newHead = Node(value)
        newHead.next = self.head
        self.head = newHead

    def removeNode(self, value):
        if self.head == None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while(current.next != None):
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next


def removeDuplicates(linked_list):
    if linked_list.head == None:
        return
    
    head = linked_list.head
    current = head
    nodes = set()
    nodes.add(head.value)

    while (current.next != None):
        if (current.next.value in nodes):
            current.next = current.next.next
            continue
        else:
            nodes.add(current.next.value)
        current = current.next
        linked_list.printList()
    
    return linked_list
    

if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.appendNode(5)
    linked_list.appendNode(6)
    linked_list.appendNode(7)
    linked_list.printList()
    
    linked_list.prependNode(1)
    linked_list.printList()

    linked_list.removeNode(6)
    linked_list.printList()

    linked_list.appendNode(1)
    linked_list.appendNode(5)
    linked_list.appendNode(6)
    linked_list.appendNode(7)
    linked_list.printList()

    removeDuplicates(linked_list)
    linked_list.printList()
