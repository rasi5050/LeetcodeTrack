# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # res=set()
        # while head:
        #     if id(head) not in res:
        #         res.add(id(head))
        #         head=head.next
        #     else:
        #         return True
        # return False
        
        #two pointer method
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:return True
        return False
        