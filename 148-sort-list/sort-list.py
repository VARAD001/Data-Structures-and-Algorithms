# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        return self.mergeSort(head)

    def mergeSort(self,head1):
        if head1 == None or head1.next == None:
            return head1
        
        fast = head1.next
        slow = head1
        while fast and fast.next:
            slow = slow.next    
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.mergeSort(head1)
        right = self.mergeSort(mid)
        return self.sorting(left,right)
        

    def sorting(self,head1,head2):
        a = head1
        b = head2
        dummy = ListNode(0)
        current = dummy
        while a and b:
            if a.val > b.val:
                current.next = b
                current = current.next
                b = b.next
            else:
                current.next = a
                current = current.next
                a = a.next
        current.next = a or b
        return dummy.next

        

        