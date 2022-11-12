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
        #intuition: complete help from leetcode discussion: (https://leetcode.com/problems/linked-list-cycle/discuss/2656867/List-Set-and-Two-Pointer-solutions-simply-explained)
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False