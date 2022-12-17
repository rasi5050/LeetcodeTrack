# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #intuition: implement recursion similar to studied in haskell (SPFM: sem1;MSCS fall22 Syracuse university)
        #recursive approach
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        """
        #status: correct
        #analysis: time O(n), Space O(1)
        #ref: 12/17/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day53/54,1.largestRectangleInHistogramTImed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.study:tree-x1pomo(7:30-8:00),4.maximumDepthOfABinaryTreeTimed25Mins-x1pomo(8:00-8:30),5.implement-x2pomo(8:30-9:30),6.invert/flipBinaryTreeTimed25Mins-x1pomo(9:30-10:00),7.implement-x2pomo(10:00-11:00),8.lowestCommonAncestorOfABinaryTreeTimed25Mins-x1pomo(10:00-10:30),9.absorber-x1pomo(10:30-11:00)=x12pomo(6:00-12:00)
        
        #iterative approach: use bfs, number of levels will be max height of tree
        frontier=[]
        if root: frontier.append(root)
        level=0
        while frontier:
            next=[]
            level+=1
            for curNode in frontier:
                if curNode.left: next.append(curNode.left)
                if curNode.right: next.append(curNode.right)
            frontier=next
        return level
        
        
        

        
        
            
        