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
    
    #status: correct
    #analysis: Time O(n logn); involves sorting, Space O(n); storing the values in list
    #ref: 12/20/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day56/56,1.constructBinaryTreeFromPreorderAndInorderTraversalTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.serializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.validateBinarySearchTreeTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.kThSmallestElementInABstTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)
