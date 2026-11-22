# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        pre = head
        after = head.next
        while after:
            while after and pre.val == after.val:
                after = after.next
            pre.next = after
            pre = after
            after = after.next if after else None
        return head





































































































        