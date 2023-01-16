# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited=set()
        while head:
            if id(head) in visited:
                return True
            visited.add(id(head))
            head=head.next
        return False