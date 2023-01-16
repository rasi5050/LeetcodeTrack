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
    
    #status: correct
    #Analysis: Time O(n), Space O(n)
    #ref: 1/16/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day83/84C3Ai3QuestionsFromMostFrequentListOf3/10Day3/5+Blind75WeekOne7/14q,2q/dayDay3/7-,1.balancedBinaryTreeTImed25Mins-x1pomo(12:30-13:00),2.linkedListCycleTimed25Mins-x1pomo(13:00-13:30),3.implement-x1pomo(13:30-14:00),4.implementQueueUsingStacksTimed25Mins-x1pomo(14:00-14:30),5.firstBadVersionTimed25Mins-x1pomo(14:30-15:00),6.implement-x1pomo(15:00-15:30),7.ransomNoteTImed25Mins-x1pomo(15:30-16:00),8.implement-x1pomo(16:00-16:30)=x8pomo(12:30-16:30)  
    
        #alter; floyd cycle detection algorithm
        slow=head
        fast=head.next
        
        while fast:
            if slow==fast:
                return True
            slow=slow.next
            fast=fast.next.next
        return False
