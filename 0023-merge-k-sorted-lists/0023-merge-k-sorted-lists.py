# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeList(l1,l2):
            temp=head=ListNode()
            while l1 and l2:
                if l1.val<=l2.val:
                    temp.next=l1
                    l1=l1.next
                else:
                    temp.next=l2
                    l2=l2.next
                temp=temp.next
            if l1:temp.next=l1
            if l2:temp.next=l2
            return head.next
        #intuition: merge in pairs;help from neetcode youtube solution(https://www.youtube.com/watch?v=q5a5OiGbT6Q)
        if len(lists)==0 or not lists:
            return None
        while len(lists)>1:
            mergedList=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                mergedList.append(mergeList(l1,l2))
            lists=mergedList
        return lists[0]
    
        