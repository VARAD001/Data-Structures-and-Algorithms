class Node:
    def __init__(self,value= 0,prev=None, next= None):
        self.value = value
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(value=homepage)
        

    def visit(self, url: str) -> None:
        if self.current.next:
            self.current.next.prev = None
        self.current.next = Node(url)
        self.current.next.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current.prev:
                self.current = self.current.prev
            else:
                break 
        return self.current.value

        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current.next:
                self.current = self.current.next
            else:
                break 
        return self.current.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)