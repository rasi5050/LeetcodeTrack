# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """        
        while head.next:
            temp=head.next
            curr=head
            next=head.next
            next.next=curr
            head=temp
            
        return head
        """
        prev, curr = None, head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        