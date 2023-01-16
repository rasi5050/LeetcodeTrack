# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        #cases:
        both nodes less than root or both nodes greater than root
        node1<root<node2 or node1>root>node2
        one node as root and other in its left or right tree
        """
        def recurse(root):
            if p.val<=root.val<=q.val or p.val>=root.val>=q.val:
                return root
            if p.val<root.val and q.val<root.val:
                return recurse(root.left)
            if p.val>root.val and q.val>root.val:
                return recurse(root.right)
        return recurse(root)
    
        #status: correct
        #Analysis: Time O(number of nodes)=O((2^h)-1)=O(2^h), where h is the height of the tree
        #Space O(1)
        #ref: 1/16/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day83/84C3Ai3QuestionsFromMostFrequentListOf3/10Day3/5+Blind75WeekOne7/14q,2q/dayDay3/7-,1.Pairs of Songs With Total Durations Divisible by 60Timed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.Sort Array by Increasing FrequencyTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.beatifulArrangementTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.dailyTemperaturesTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),Blind75WeekOne1;9.Lowest Common Ancestor of a Binary Search TreeTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  
