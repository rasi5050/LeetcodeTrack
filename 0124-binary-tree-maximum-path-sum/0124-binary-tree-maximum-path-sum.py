# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def  maxPathSum(self, root: Optional[TreeNode]) -> int:
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