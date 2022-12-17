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
            # return flip(root.left) or flip(root.right)
            #or the recursive part can be independent calls on left and right
            flip(root.left)
            flip(root.right)
            
        flip(root)
        return root