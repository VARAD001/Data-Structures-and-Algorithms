# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        temp = head
        listed = []
        while temp:
            listed.append(temp)
            temp = temp.next
        if len(listed) - n == 0:
            return head.next
        listed[len(listed) - n - 1].next = listed[len(listed) - n].next
        return head

        