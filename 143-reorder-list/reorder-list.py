# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        def rec(root, current):
            if not current:
                return root
            root = rec(root, current.next)
            if not root:
                return None
            temp = None
            if root == current or root.next == current:
                current.next = None
            else:
                temp = root.next
                root.next = current
                current.next = temp
            return temp
        head = rec(head,head.next)
        