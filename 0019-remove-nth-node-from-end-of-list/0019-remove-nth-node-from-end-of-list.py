# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: #null case
            return None
        back=front=head
        for _ in range(n):  #moving front pointer ahead
            front=front.next
        if front==None:     #n==len(list)
            return head.next
        while front.next:
            back=back.next
            front=front.next
        back.next=back.next.next
        return head
    
    #status: correct
    #ref: 11/13/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day37/38:do,1.mergeKSortedListsTimed25Mins-x1pomo(12:00-12:30),2.implement-x2pomo(12:30-13:30),3.removeNthNodeFromEndOfListTimed25Mins-x1pomo(13:30-14:00),4.implement-x2pomo(14:00-15:00),5.reorderListTimed25Mins-x1pomo(15:00-15:30),6.implement-x2pomo(15:30-16:30),7.studyQueue-x1pomo(16:30-17:00),8.stackUsingQueuesTimed25Mins-x1pomo(17:00-17:30),9.implement-x2pomo(17:30-18:30)=x13pomo(12:00-18:30)

        
            