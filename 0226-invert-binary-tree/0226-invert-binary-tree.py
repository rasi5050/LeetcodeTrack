# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def flip(root):
            #<some base case: putting end to recursion>
            if not root:
                return 
            #<flipping part>
            root.left, root.right = root.right, root.left
            #recursive part
            return flip(root.left) or flip(root.right)
            """
            #or the recursive part can be independent calls on left and right
            flip(root.left)
            flip(root.right)
            """
        flip(root)
        return root
    
    #status: correct
    #analysis: Time O(n) all nodes visited, Space O(1): nothing stored
    #ref: 12/17/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day53/54,1.largestRectangleInHistogramTImed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.study:tree-x1pomo(7:30-8:00),4.maximumDepthOfABinaryTreeTimed25Mins-x1pomo(8:00-8:30),5.implement-x2pomo(8:30-9:30),6.invert/flipBinaryTreeTimed25Mins-x1pomo(9:30-10:00),7.implement-x2pomo(10:00-11:00),8.lowestCommonAncestorOfABinaryTreeTimed25Mins-x1pomo(10:00-10:30),9.absorber-x1pomo(10:30-11:00)=x12pomo(6:00-12:00)
    
    #concise solution from leetcode discussion: StefanPochmann (https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python)
