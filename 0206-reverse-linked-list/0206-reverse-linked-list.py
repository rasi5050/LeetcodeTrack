# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         head2=ListNode() #pointer to result
#         tempHead=head2
#         res=[]
#         def reverseLl(head):
#             nonlocal tempHead
#             if head.next:
#                 reverseLl(head.next)
#             tempHead.next=ListNode(head.val)
            
#             print(tempHead)
#         reverseLl(head)
#         return head2

        #approach2: reverse direction(from leetcode discussion)
        prev=None
        cur=head
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev
        #approach3: reverse direction iterative changed to recursive(neetcode youtube comments:https://www.youtube.com/watch?v=G0_I-ZF0S38)
        
        # prev=None
        # def reverseLl(prev,head):
        #     if not head: return prev
        #     while head:
        #         next=head.next
        #         head.next=prev
        #         return reverseLl(head,next)
        # return reverseLl(prev,head)
        