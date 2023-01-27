# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        count=0
        if not root: return 0
    
        #post order
        def recurse(root):
            nonlocal count
            if not root:
                return []
            if not root.left and not root.right: #this is like returning [1] from node 4 in the first example
                return [1]
            leftDistances=recurse(root.left)
            rightDistances=recurse(root.right)
            
            for leftD in leftDistances:
                if leftD>distance:  #if one of the parameter is greater, their sum is going to be greater, hence no point in calculating
                    continue
                for rightD in rightDistances:
                    if leftD+rightD<=distance:
                        count+=1
            return [1+d for d in leftDistances+rightDistances]
        recurse(root)
        return count