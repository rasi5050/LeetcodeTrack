# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recurse(preorder, inorder):
            if not preorder:
                return None
            node=TreeNode(preorder[0])
            
            i=inorder.index(preorder[0])            
            node.left=recurse(preorder[1:i+1], inorder[:i])
            node.right=recurse(preorder[i+1:], inorder[i+1:])
            return node
        return recurse(preorder, inorder)
            
        #storing global inorder indexes doesnt work because, when the preorder is divided and recursed
        #the inorder should also reflect the preorder elements, then only the index will match
        
        
        