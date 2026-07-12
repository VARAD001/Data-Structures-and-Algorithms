# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre = None
        after = slow
        while slow:
            after = slow.next
            slow.next = pre
            pre = slow
            slow = after
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        
        return True
        