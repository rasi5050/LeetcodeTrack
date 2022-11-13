# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=temp=ListNode()
        while list1 and list2:
            # print(head.next)
            if list1.val<=list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        if not list1 and list2:
            temp.next=list2
        elif not list2 and list1:
            temp.next=list1
        return head.next
    
            
                
        