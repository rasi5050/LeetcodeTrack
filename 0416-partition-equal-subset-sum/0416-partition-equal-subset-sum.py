class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #idea: get elements to match half the sum, then it will be two equal subset sums
        #create all combinations and check their sum
        """Rasi's answer ; correct;TLE
        totalSum=sum(nums)
        if totalSum%2: return False
        halfSum=totalSum//2
        visited=set()
        @cache
        def dfs(i,curSum):
            # print(curSum)
            if curSum==0:
                return True
            if curSum<0:
                return False
            for i,v in enumerate(nums):
                if i not in visited:
                    visited.add(i)
                    if dfs(i,curSum-v)==True:
                        return True
                    visited.remove(i)
            return False
            
        return dfs(0,halfSum)
        """
        totalSum=sum(nums)
        if totalSum%2: return False
        halfSum=totalSum//2

        @cache
        def dfs(i,curSum):
            # print(curSum)
            if curSum==0:
                return True
            if curSum<0 or i>=len(nums):
                return False
            return dfs(i+1,curSum-nums[i]) or dfs(i+1,curSum)
        
        return dfs(0,halfSum)

        #status: correct; help(https://leetcode.com/problems/partition-equal-subset-sum/discuss/1624939/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Bitmask)  
        #Analysis: Time O(N*Sum), SPace O(N*Sum)
        #ref: 2/10/2023P2:track1-cpGrind75;Day106/106;doLeetcodeBlind75-3q/day-20/45Q:completeOn2/15/2023-Day14/15,collateQuestionPatternIntoCategoriesAndTemplate-Day5/5:(addWordDescriptionOnceProblemIsSolvedDay4/4),               ,1.partitionEqualSubsetSumTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.stringToIntegerTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.absorber-x1pomo(9:00-9:30),6.applyInternships(0.(P2:searchInternshipInTiktokWebsite(https://careers.tiktok.com/position/7138620933615733006/detail);1.Please state your availability clearly in your resume (Start date, End date).(1. May 22, 2023 to August 11, 2023),2.applyOtherPositionIfAllowed,3.addDockerExperienceToResume),3.https://adelatech.com/adelatech-jobs/cloud-architect-and-devops-intern-apprentice/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,4.https://www.monster.com/job-openings/software-engineer-devops-summer-internship-weston-ma--9526b6fa-3381-4622-9d6f-5d023867f090?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,5.https://www.ziprecruiter.com/c/Bose-Corporation/Job/Security-DevOps-Engineering-Intern/-in-Framingham,MA?jid=a053022317016772&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,6.https://ct.tarta.ai/j/14FJ14QBvf0LOA5Ejt3O1222-devops-engineer-intern-in-danbury-connecticut-at-experian?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic)-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

