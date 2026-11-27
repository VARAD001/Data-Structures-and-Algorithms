class Node:
    def __init__(self, val, pre, next):
        self.value = val
        self.next= next
        self.prev = pre

class MyCircularDeque:

    def __init__(self, k: int):
        self.left = Node(0,None,None)
        self.right = Node(0, self.left, None)
        self.left.next = self.right
        self.space = k
        

    def insertFront(self, value: int) -> bool:
        if self.space == 0:
            return False
        pre = self.right.prev
        next = self.right
        newnode = Node(value,None,None)
        pre.next = next.prev = newnode
        newnode.next = next
        newnode.prev = pre
        self.space -= 1
        return True

        

    def insertLast(self, value: int) -> bool:
        if self.space == 0:
            return False
        pre = self.left
        next = self.left.next
        newnode = Node(value,None,None)
        pre.next = next.prev = newnode
        newnode.next = next
        newnode.prev = pre
        self.space -= 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        pre = self.right.prev.prev
        next = self.right
        pre.next = next
        next.prev = pre
        self.space += 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False        
        pre = self.left
        next = self.left.next.next
        pre.next = next
        next.prev = pre
        self.space += 1
        return True        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.value
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.value
        

    def isEmpty(self) -> bool:
        return self.left.next == self.right
        

    def isFull(self) -> bool:
        return self.space == 0
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()