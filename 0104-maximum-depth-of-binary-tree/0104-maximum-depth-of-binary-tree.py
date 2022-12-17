# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #intuition: implement recursion similar to studied in haskell (SPFM: sem1;MSCS fall22 Syracuse university)
        #recursive approach
        if root==None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
            
        