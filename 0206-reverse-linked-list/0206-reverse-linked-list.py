# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """        
        while head.next:
            temp=head.next
            curr=head
            next=head.next
            next.next=curr
            head=temp
            
        return head
        """
        prev, curr = None, head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        
        #status: correct; copy from neetcode youtube solution(https://www.youtube.com/watch?v=G0_I-ZF0S38)
        #Analysis: Time O(n), Space O(1)
        #ref: 1/17/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day84/84C3Ai3QuestionsFromMostFrequentListOf7/10Day4/5+Blind15/75,2q/dayDay4/7;1.binarySubArraysWithSumTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.generateParenthesesTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.serializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.climbingStairsTimed25Mina-x1pomo(9:00-9:30),8.longestPalindromeTimed25Mins-x1pomo(9:30-10:00),9.reverseLinkedListTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  

        #