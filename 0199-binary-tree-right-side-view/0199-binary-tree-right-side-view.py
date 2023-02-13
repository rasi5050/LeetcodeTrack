# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        currRightLevelMax=-1
        def dfs(i,root):
            nonlocal currRightLevelMax
            if not root:
                return
            if (i>currRightLevelMax): res.append(root.val)
            currRightLevelMax=max(currRightLevelMax,i)
            dfs(i+1,root.right)
            dfs(i+1,root.left)
            
        dfs(0,root)
        return res
        
        #status: correct
        #Analysis: Time O(2^n), Space O(2^n)
        #ref:2/13/2023P2:track1-cpGrind75;Day108/108;doLeetcodeBlind75-3q/day-  23/45Q:completeOn2/15/2023-Day16/15,collateQuestionPatternIntoCategoriesAndTemplate-Day7/5:(addWordDescriptionOnceProblemIsSolvedDay5/4),1.subsetsTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),4.2/13/2023prepareForAbbvieInterviewDay1/3,1.createFocusPoints-x1pomo(7:30-8:00)
#2/13/2023prepareForAbbvieInterviewDay1/3,1.checkInterviewerProfile,jd-x1pomo(8:00-8:30),5.absorber-x1pomo(8:30-9:00),6.applyInternship-x5DevOps-x2pomo(9:00-10:00),7.applyInternships-x5SWEFromGitHubPage-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

            
            