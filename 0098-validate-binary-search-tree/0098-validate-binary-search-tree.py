# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #intuition: use inorder traversal and check the resultant array is sorted
        """ working code: commented for alternate approach
        res=[]
        def dfs(node):
            if not node : return    
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)   
        dfs(root)
        return sorted(set(res))==res
        """
    
    #status: correct
    #analysis: Time O(n logn); involves sorting, Space O(n); storing the values in list
    #ref: 12/20/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day56/56,1.constructBinaryTreeFromPreorderAndInorderTraversalTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.serializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.validateBinarySearchTreeTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.kThSmallestElementInABstTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)
        """wrong code: just checking left and right is not enough, since in 
[5,4,6,null,null,3,7], although 3<6<7, 3 should be in the left branch of 4
        def dfs(node):
            if not node.left and not node.right: return True
            
            elif node.left and node.right:
                return node.left.val<node.val<node.right.val and dfs(node.left) and dfs(node.right)
            elif node.left:
                return node.left.val<node.val and dfs(node.left)
            else:
                return node.val<node.right.val and dfs(node.right)
        return dfs(root)==True
        """
        #optimize sort code for O(n)
        """ working code
        res=[]
        def dfs(node):
            if not node : return    
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)   
        dfs(root)
        for i in range(len(res)-1):      #O(n)
            if res[i]>=res[i+1]: return False   
        return True
        """
        #status: correct; improved runtime complexity
        #Analysis: Time O(n); only adjacent elements has to be checked for sorted, Space O(n)
        #ref: #ref: 12/20/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day56/56,1.constructBinaryTreeFromPreorderAndInorderTraversalTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.serializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.validateBinarySearchTreeTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.kThSmallestElementInABstTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)
        def checker(root, lower, upper):
            if not root: 
                return True
            if lower>=root.val or upper<= root.val:
                return False
            else:
                return checker(root.left, lower, root.val) and checker(root.right, root.val, upper)
        return checker(root, -math.inf, math.inf)
        