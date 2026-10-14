class MyHashMap:

    def __init__(self):
        self.map = [[] for _ in range(43)]

    def _hash(self,key):
        hashed_value = 0
        for char in str(key):
            hashed_value = ((hashed_value + ord(char)*23)%43)
        return hashed_value
        

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for i, (keys,values) in enumerate(self.map[index]):
            if keys == key:
                self.map[index][i] = (key,value)
                return
        self.map[index].append((key,value))
        
        
        

    def get(self, key: int) -> int:
        index = self._hash(key)
        for stored_key,stored_value in self.map[index]:
            if stored_key == key:
                return stored_value
        return (-1)
            
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        for i,(stored_key,stored_value) in enumerate(self.map[index]):
            if stored_key == key:
                self.map[index].pop(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)