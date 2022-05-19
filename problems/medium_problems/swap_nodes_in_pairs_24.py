# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = d = ListNode(0)
        dummyNode.next = head
        
        while d.next and d.next.next:
            # initialize
            p = d.next
            q = d.next.next
            
            # set new positions
            d.next = q
            p.next = q.next
            q.next = p
            
            # set up next positions
            d = p
            
        return dummyNode.next
