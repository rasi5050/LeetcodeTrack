# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) and (not q): #base condition
            return True         #implicit condition, if nodes are not matching, it will not satisfy any condition, hence that recursive call will return False by default 
        elif (p and q) and (p.val==q.val):  #recursive step
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        #status: correct
        #analysis: Time O(n): visiting all nodes, 
        #Space O(1) nothing being stored
        #ref: 12/17/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day53/54,1.largestRectangleInHistogramTImed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.study:tree-x1pomo(7:30-8:00),4.maximumDepthOfABinaryTreeTimed25Mins-x1pomo(8:00-8:30),5.implement-x2pomo(8:30-9:30),6.invert/flipBinaryTreeTimed25Mins-x1pomo(9:30-10:00),7.implement-x2pomo(10:00-11:00),8.lowestCommonAncestorOfABinaryTreeTimed25Mins-x1pomo(10:00-10:30),9.absorber-x1pomo(10:30-11:00)=x12pomo(6:00-12:00)
        #observation: able to do recursive questions easily due to the skill haskell programming from MSCS Fall22 sem1; course=SPFM: Prof: andrew ChengYung Lee
