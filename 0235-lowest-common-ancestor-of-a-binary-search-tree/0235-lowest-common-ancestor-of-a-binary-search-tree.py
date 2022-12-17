# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #identify a branching, return the current node
        if (p.val <= root.val or q.val <= root.val) and (p.val >= root.val or q.val >= root.val): return root
        elif (p.val <= root.val and q.val <= root.val): return self.lowestCommonAncestor(root.left, p, q)
        else: return self.lowestCommonAncestor(root.right, p, q)
        
        #status: correct
        #analysis: Time O(log n) might have to traverse till height of tree
        #Space O(1): stores nothing
        #ref: 12/17/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day53/54,1.largestRectangleInHistogramTImed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.study:tree-x1pomo(7:30-8:00),4.maximumDepthOfABinaryTreeTimed25Mins-x1pomo(8:00-8:30),5.implement-x2pomo(8:30-9:30),6.invert/flipBinaryTreeTimed25Mins-x1pomo(9:30-10:00),7.implement-x2pomo(10:00-11:00),8.lowestCommonAncestorOfABinaryTreeTimed25Mins-x1pomo(10:00-10:30),9.absorber-x1pomo(10:30-11:00)=x12pomo(6:00-12:00)

        