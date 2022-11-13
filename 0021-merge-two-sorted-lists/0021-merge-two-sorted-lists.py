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
    
    #status: correct
    #ref:11/12/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day37/38:do,1.mergeTwoSortedListTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x3pomo(18:00-19:30)
    
            
                
        