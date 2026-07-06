# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        temp = dummy
        while list1 and list2:
            if list1.val > list2.val:
                current = list2
                list2 = list2.next
                temp.next = current
                temp = temp.next
                current.next = None
            else:
                current = list1
                list1 = list1.next
                temp.next = current
                temp = temp.next
                current.next = None
        if list1 is not None:
            temp.next = list1
        elif list2 is not None:
            temp.next = list2
        return dummy.next
            

            
                
        
