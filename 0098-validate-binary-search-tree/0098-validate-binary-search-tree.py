# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """commented to try alter
        #idea:inorder traversal should return sorted list
        res=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        # print(res)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True
        """
    #status: correct
    #Analysis: Time O(n), Space O(n)
    #ref: 1/29/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day97/98Blind35/75;doLeetcodeBlind75-3q/day-5/45Q:completeOn2/15/2023-Day3/15:1.P1:1.numberOfWeakCharactersInTheGameTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.coinChangeTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.productOfArrayExceptSelfTimed25Mins-x1pomo(8:00-8:30),6.minStackTimed25Mins-x1pomo(8:30-9:00),7.validateBinarySearchTreeTimed25Mins-x1pomo(9:00-9:30),8.numberOfIslandsTimed25Mins-x1pomo(9:30-10:00),9.rottingOrangesTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

    
        #alter
        
        def dfs(root, left, right):
            if not root:
                return True
            elif left>=root.val or right<=root.val:
                return False
            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        return dfs(root, -math.inf, math.inf)
        
    
    