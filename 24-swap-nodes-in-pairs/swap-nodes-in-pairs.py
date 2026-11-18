# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0,head)
        pre = dummy
        current = head
        after = head
        while current:
            if not current.next:
                return dummy.next
            after = current.next.next
            pre.next = current.next
            current.next.next = current
            current.next = after
            pre = current
            current = after
        return dummy.next

        