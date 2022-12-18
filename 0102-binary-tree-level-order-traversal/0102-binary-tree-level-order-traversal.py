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
    #status: correct
    #analysis: Time O(n), Space O(n)
    #ref: 12/18/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day54/54,1.binaryTreeMaximumPathSumTimed25Mins-x1pomo(7:00-7:30),2.implement-x2pomo(7:30-8:30)=x3pomo(7:00-8:30)
