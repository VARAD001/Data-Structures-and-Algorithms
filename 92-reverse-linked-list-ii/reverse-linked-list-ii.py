# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right:
            return head
        current = head
        pre = None
        for _ in range(left - 1):
            pre = current
            current = current.next
        before = None
        first = pre.next if pre else head
        for _ in range(right - left + 1):
            after = current.next
            current.next = before
            before = current
            current = after
        if pre:
            pre.next = before
        else:
            head = before
        first.next = after
        return head
        
         
        