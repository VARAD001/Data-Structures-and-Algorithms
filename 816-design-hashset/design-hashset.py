class MyHashSet:

    def __init__(self):
        self.hash_set = [[] for _ in range(1009)]

    def _hash(self,key):
        return key % 1009
        
    def add(self, key: int) -> None:
        index = self._hash(key)
        if key not in self.hash_set[index]:
            self.hash_set[index].append(key)
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.hash_set[index]:
            self.hash_set[index].remove(key)
        
    def contains(self, key: int) -> bool:
        index = self._hash(key)
        if key in self.hash_set[index]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)