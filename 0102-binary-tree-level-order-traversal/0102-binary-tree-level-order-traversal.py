# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        frontier=[]
        if root: frontier=[root]
        while frontier:
            next=[]
            temp=[]
            for node in frontier:
                temp.append(node.val)
                if node.left: next.append(node.left)
                if node.right: next.append(node.right)
            frontier=next[:]
            res.append(temp)
        return res