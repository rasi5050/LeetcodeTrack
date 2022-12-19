# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in {None, p, q}: return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right: return root
        elif left: return left
        else: return right
        
        #status: success: help from https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/1306476/C%2B%2BPython-2-solutions-Clean-and-Concise-O(N)
        #analysis: Time O(n); visiting all nodes, Space O(1); nothing stored
        #ref: 12/19/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day55/56,1.lowestCommonAncestorOfABinaryTreeTimed25Mins-x1pomo(10:00-10:30),2.implement-x2pomo(10:30-11:30)-x3pomo(10:00-11:30)

        