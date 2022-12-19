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
    
    #status: correct
    #analysis: Time O(n); although only right side is only required, all nodes are visited and kept track. cannot predict which would be the right most side in the next level. a left branch would be the one visible from right if right brach in not present.
    #Space O(n): storing the values in res + temp values in frontier and next
    #ref: 12/19/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day55/56,1.binaryTreeRightSideViewTImed25Mins-x1pomo(12:00-12:30),2.implement-x2pomo(12:30-13:30),3.subtreeOfAnotherTreeTimed25Mins-x1pomo(13:30-14:00),4.implement-x2pomo(14:00-15:00),5.absorber-x1pomo(15:00-15:30)=x6pomo(12:00-15:30)
