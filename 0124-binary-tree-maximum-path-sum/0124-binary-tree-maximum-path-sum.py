# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def  maxPathSum(self, root: Optional[TreeNode]) -> int:
        #intuition from neetcode youtube solution (https://www.youtube.com/watch?v=Hr5cWUld4vU&t=1s)
        res=[root.val]
        def recurse(root): 
            if not root:
                return 0
            l=max(recurse(root.left),0)
            r=max(recurse(root.right),0)
            res[0]=max(res[0], l+r+root.val)
            return root.val + max(l, r)
        recurse(root)
        return res[0]
    
    #status: correct
    #analysis: Time O(n), Space O(1)
    #ref: 12/18/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day54/54,1.binaryTreeMaximumPathSumTimed25Mins-x1pomo(7:00-7:30),2.implement-x2pomo(7:30-8:30)=x3pomo(7:00-8:30)
