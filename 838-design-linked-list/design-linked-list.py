class Node:
    def __init__(self, value=0 , next_node=None):
        self.value = value
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if current:
                current = current.next
            else:
                return -1
        if current:
            return current.value
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        if not self.head:
            self.head = newnode
            self.tail = newnode
            self.length = 1
            return
        newnode.next = self.head
        self.head = newnode
        self.length += 1
        return
        

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if not self.head or self.length == 0:
            self.head = newnode
            self.tail = newnode
            self.length = 1
            return
        self.tail.next = newnode
        self.tail = self.tail.next
        self.length += 1
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if not self.head:
            return self.addAtHead(val)
        if index == 0:
            return self.addAtHead(val)
        if index == self.length :
            return self.addAtTail(val)
        current = self.head
        for _ in range(index - 1):
            if current:
                current = current.next
            else:
                return
        if current:
            current.next = Node(val, current.next)
        self.length += 1
        return None


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        if current.next == self.tail:
            self.tail = current
        current.next = current.next.next
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)