import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        for ll  in lists:
            while ll:
                heapq.heappush(res, ll.val)
                ll=ll.next
        root=carrier=ListNode()        
        while res:
            carrier.next=ListNode(heapq.heappop(res))
            carrier=carrier.next
        return root.next
                
        