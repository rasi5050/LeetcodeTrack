# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #intuition: inorder traversal will give sorted order;select (k-1)th from it
        res=[]
        def dfs(node):
            if not node: return 
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res[k-1]
    #status: correct
    #analysis: Time O(n); visiting all nodes for inorder traversal, Space O(n); storing inorder traversal
    #ref:12/21/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day57/58,1.kThSmallestElementInABstTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.study:graph-x1pomo(7:00-7:30),4.numberOfIslandsTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.floodFillTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.01MatrixTimed25Mins-x1pomo(10:30-11:00),9.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)
