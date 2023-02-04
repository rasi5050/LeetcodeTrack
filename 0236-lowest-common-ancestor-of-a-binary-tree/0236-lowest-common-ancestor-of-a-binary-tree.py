# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca=None
        def recurse(root):
            nonlocal lca
            if not root:
                return False

            left,right=recurse(root.left), recurse(root.right)
           
            curr = root==p or root==q
            if curr+left+right>=2:
                lca=root
            return curr or left or right
        recurse(root)
        return lca