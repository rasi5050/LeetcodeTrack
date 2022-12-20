# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #intuition: use inorder traversal and check the resultant array is sorted
        res=[]
        def dfs(node):
            if not node : return    
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)   
        dfs(root)
        return sorted(set(res))==res
    