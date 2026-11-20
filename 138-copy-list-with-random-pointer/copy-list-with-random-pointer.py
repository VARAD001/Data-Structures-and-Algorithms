"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtonew = collections.defaultdict(lambda: Node(0))
        oldtonew[None] = None
        current = head
        while current:
            oldtonew[current].val = current.val
            oldtonew[current].next = oldtonew[current.next]
            oldtonew[current].random = oldtonew[current.random]
            current = current.next
        return oldtonew[head]