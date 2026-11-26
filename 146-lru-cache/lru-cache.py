class Node:
    def __init__(self,key = 0, value=0,next=None, pre= None):
        self.value = value
        self.key = key
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.buffer = {}    
        self.left = Node()
        self.right = Node(pre=self.left)
        self.left.next = self.right

    def remove(self,old):
        before = old.pre
        after = old.next
        before.next = after
        after.pre = before

    def insert(self,new):
        before = self.right.pre
        after = self.right
        before.next = after.pre = new
        new.next, new.pre = after, before
        

    def get(self, key: int) -> int:
        if key in self.buffer:
            self.remove(self.buffer[key])
            self.insert(self.buffer[key])
            return self.buffer[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.buffer:
            self.remove(self.buffer[key])
        self.buffer[key] = Node(key=key, value=value)
        self.insert(self.buffer[key])
        if len(self.buffer) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.buffer[lru.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)