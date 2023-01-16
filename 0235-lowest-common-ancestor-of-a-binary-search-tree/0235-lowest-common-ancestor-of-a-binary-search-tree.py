# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        #cases:
        both nodes less than root or both nodes greater than root
        node1<root<node2 or node1>root>node2
        one node as root and other in its left or right tree
        """
        def recurse(root):
            if p.val<=root.val<=q.val or p.val>=root.val>=q.val:
                # print(p.val,root.val,q.val)
                return root
            if p.val<root.val and q.val<root.val:
                return recurse(root.left)
            if p.val>root.val and q.val>root.val:
                return recurse(root.right)
            
        return recurse(root)