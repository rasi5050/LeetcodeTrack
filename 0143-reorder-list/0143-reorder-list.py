# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """     
        #intuition: split into half, reverse second half and rearrachnge(half help from neetcode youtube solution(https://www.youtube.com/watch?v=S5bfdUTrKLM))
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse link of second half
        second=slow.next
        prev=slow.next=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        while prev:
            temp=head.next
            head.next=prev
            prev=prev.next
            head.next.next=temp
            head=head.next.next
        #status: correct
        #ref:11/13/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day37/38:do,1.mergeKSortedListsTimed25Mins-x1pomo(12:00-12:30),2.implement-x2pomo(12:30-13:30),3.removeNthNodeFromEndOfListTimed25Mins-x1pomo(13:30-14:00),4.implement-x2pomo(14:00-15:00),5.reorderListTimed25Mins-x1pomo(15:00-15:30),6.implement-x2pomo(15:30-16:30),7.studyQueue-x1pomo(16:30-17:00),8.stackUsingQueuesTimed25Mins-x1pomo(17:00-17:30),9.implement-x2pomo(17:30-18:30)=x13pomo(12:00-18:30)
#analysis: time O(n)
#space O(1), only constant varibales used for extra memory
        
        
        
            

            