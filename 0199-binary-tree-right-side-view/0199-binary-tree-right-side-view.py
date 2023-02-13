# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        currRightLevelMax=-1
        def dfs(i,root):
            nonlocal currRightLevelMax
            if not root:
                return
            if (i>currRightLevelMax): res.append(root.val)
            currRightLevelMax=max(currRightLevelMax,i)
            dfs(i+1,root.right)
            dfs(i+1,root.left)
            
        dfs(0,root)
        return res
        
        return []
            
            