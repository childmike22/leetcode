# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  
        dummyHead = cursor = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                cursor.next = l1
                l1 = l1.next
            else:
                cursor.next = l2
                l2 = l2.next
            cursor = cursor.next
            
        if l1:
            cursor.next = l1
        else:
            cursor.next = l2
        
        return dummyHead.next
