# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        current = head
        LList = []
        while current:
            LList.append(current)
            current = current.next
        for i in range(0,len(LList) - 1,2):
            LList[i], LList[i + 1] = LList[i + 1], LList[i]
        for i in range(len(LList)-1):
            LList[i].next = LList[i + 1]
        LList[-1].next = None
        return LList[0]
        