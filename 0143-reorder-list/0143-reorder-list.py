# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """     
        #intuition: split into half, reverse second half and rearrachnge
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse link of second half
        second=slow.next
        prev=slow.next=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        while prev:
            temp=head.next
            head.next=prev
            prev=prev.next
            head.next.next=temp
            head=head.next.next
        
        
            

            