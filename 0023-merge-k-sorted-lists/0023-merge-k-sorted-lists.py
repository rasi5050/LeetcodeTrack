import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
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
    """
    #status: correct
    #Analysis: TimeO(nlogn), heappush is logn, that is repeated number of nodes time, ie. n, hence n logn
    #Space O(n): n; storing all elements in res[]
    #ref: 12/24/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day60/60,1.studyHeap-x1pomo(5:30-6:00),2.mergeKSortedListsTimed25Mins-x1pomo(6:00-6:30),3.implement-x1pomo(6:30-7:30),4.kSmallestPointsToOriginTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.topKFrequentElementsTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.findMedianFromDataStreamTimed25Mins-x1pomo(10:30-11:00),9.implement-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)

        #generate linkedlist using same linkedlist
        #use heapq to store only the 1st elements(a.k.a smallest in them) and select smallest amongst them as current ll node
        h=[]
        for i, ll in enumerate(lists):
            if ll: heapq.heappush(h, (ll.val, i))
        print(h)
        head=cur=ListNode()
        while(h):
            val, i = heapq.heappop(h)
            cur.next=ListNode(val)
            cur=cur.next
            node = lists[i] = lists[i].next
            if node:
                heapq.heappush(h, (node.val, i))
        return head.next
        