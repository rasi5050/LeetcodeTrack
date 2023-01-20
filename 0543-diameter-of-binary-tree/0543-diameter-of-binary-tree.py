# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia=0
        def recurse(root):
            nonlocal maxDia
            if not root:
                return 0
            left = recurse(root.left)
            right = recurse(root.right)
            maxDia=max(maxDia, left+right)
            return max(left, right) + 1
        recurse(root) 
        return maxDia
            
        