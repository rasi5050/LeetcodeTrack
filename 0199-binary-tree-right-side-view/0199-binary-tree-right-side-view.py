# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res=[root.val]
        frontier=[root]
        while frontier:
            next=[]
            for node in frontier:
                if node.left: next.append(node.left)
                if node.right: next.append(node.right)
            frontier=next[:]
            if next: res.append(next.pop().val)
        return res