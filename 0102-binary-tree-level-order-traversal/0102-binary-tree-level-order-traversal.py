# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #do BFS
        res=[]
        frontier=[root]
        while frontier:
            next=[]
            temp=[]
            for node in frontier:
                if node:
                    temp.append(node.val)
                    next.append(node.left)
                    next.append(node.right)    
            frontier=next
            res.append(temp)
        return res[:-1]
        