# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float(-inf))
        dummy.next = head
        pre = dummy.next
        temp = pre.next
        if not head or not pre:
            return head
        while temp:
            while temp and temp.val < pre.val:
                find = dummy
                while find.next.val < temp.val:
                    find = find.next
                pre.next = pre.next.next
                temp.next = find.next
                find.next = temp
                temp = pre.next
            pre = pre.next
            if temp:
                temp = temp.next
        return dummy.next


        