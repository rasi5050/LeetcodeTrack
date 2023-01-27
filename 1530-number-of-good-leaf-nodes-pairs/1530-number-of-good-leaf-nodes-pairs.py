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
    
    #status: correct; help(https://www.youtube.com/watch?v=3JU0v2kuYGg&t=552s)
    #Analysis: Time O(N^2); nested for loop inside recursion
    #Space O(N)
    #ref: 1/27/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day94/94Blind30/75,2q/dayDay13/12;doLeetcode3Question/Day:1.P1:1.numberOfGoodLeafNodesPairsTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.productOnLastKNumbersTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.binaryTreeLevelOrderTraversalTimed25Mins-x1pomo(8:00-8:30),6.cloneGraph-x1pomo(8:30-9:00),7.Evaluate Reverse Polish NotationTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.courseSchedule-x1pomo(10:00-10:30)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)early(6:00-10:30)
