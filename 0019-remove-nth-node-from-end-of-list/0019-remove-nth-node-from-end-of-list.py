# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        back=front=head
        for _ in range(n):
            front=front.next
        print(back,front)
        if front==None:
            return head.next
        while front.next:
            back=back.next
            front=front.next
        back.next=back.next.next
        return head
        
            