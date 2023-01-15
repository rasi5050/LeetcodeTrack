# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        sentinel=trail=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                trail.next=ListNode(list1.val)
                trail,list1=trail.next,list1.next
            else:
                trail.next=ListNode(list2.val)
                trail,list2=trail.next,list2.next
        if list1:
            trail.next=list1
        if list2:
            trail.next=list2
                
        return sentinel.next