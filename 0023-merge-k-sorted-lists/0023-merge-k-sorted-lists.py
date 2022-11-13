# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #intuition: merge in pairs;half help from neetcode youtube solution(https://www.youtube.com/watch?v=q5a5OiGbT6Q)
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

        if not lists:
            return None
        while len(lists)>1:
            mergedList=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                mergedList.append(mergeList(l1,l2))
            lists=mergedList
        return lists[0]
    #idea: pair up linkedList and apply merge sort for 2 linked list
    #status: correct
    #ref: 11/13/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day37/38:do,1.mergeKSortedListsTimed25Mins-x1pomo(12:00-12:30),2.implement-x2pomo(12:30-13:30),3.removeNthNodeFromEndOfListTimed25Mins-x1pomo(13:30-14:00),4.implement-x2pomo(14:00-15:00),5.reorderListTimed25Mins-x1pomo(15:00-15:30),6.implement-x2pomo(15:30-16:30),7.studyQueue-x1pomo(16:30-17:00),8.stackUsingQueuesTimed25Mins-x1pomo(17:00-17:30),9.implement-x2pomo(17:30-18:30)=x13pomo(12:00-18:30)

        