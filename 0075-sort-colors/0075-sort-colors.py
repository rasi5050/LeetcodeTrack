class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """working code in 2 pass; commented for alter
        #use array of size 3:
        bucket=[0]*3
        for n in nums:
            bucket[n]+=1
        
        for i,v in enumerate([0]*bucket[0]+[1]*bucket[1]+[2]*bucket[2]):
            nums[i]=v
        """
        l,i,r=0,0,len(nums)-1
        for _ in range(len(nums)):
            if nums[i]==0:
                nums[l],nums[i]=nums[i],nums[l]
                i+=1
                l+=1
            elif nums[i]==2:
                nums[r],nums[i]=nums[i],nums[r]
                r-=1
            elif nums[i]==1:
                i+=1
        """
        why this works: since we have 3 distinct number we use 3 pointers representing left of l has only 0's, right of r has only 2's, and 1 is tracked by i's.
            whenever we encounter 0 in i, simply swap items in i,l. l will have non zero item or zeroed item, it may swap zero to l or non zero to l
            similarly for other partitions.
            
            when nums[i]==0, l++, i++
            when nums[i]==1, i++; we simply skip it,because its already in the correct partition.
            
        """
        #status: correct; help(https://www.youtube.com/watch?v=4xbWSRZHqac&t=781s), help(https://leetcode.com/problems/sort-colors/discuss/3108642/Java-And-Python-(Simple-And-Fast-Solution))
        #Analysis: Time O(n), Space O(1)
        #ref: 2/9/2023P2:track1-cpGrind75;Day105/106;doLeetcodeBlind75-3q/day-18/45Q:completeOn2/15/2023-Day13/15,collateQuestionPatternIntoCategoriesAndTemplate-Day4/5:(addWordDescriptionOnceProblemIsSolvedDay3/4),1.sortColorsTimed25Mins-x1pomo(6:00-6:30),2.implement(addDescriptionAfterSolvingProblem)-x1pomo(6:30-7:00),3.wordBreakTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.partitionEqualSubsetSumTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.absorber-x2pomo(9:00-10:00),8.applyInternships(0.(P2:searchInternshipInTiktokWebsite(https://careers.tiktok.com/position/7138620933615733006/detail);1.Please state your availability clearly in your resume (Start date, End date).(1. May 22, 2023 to August 11, 2023),2.applyOtherPositionIfAllowed,3.addDockerExperienceToResume)
#,1.https://www.adzuna.com/details/3913091385?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,2.https://allengerritsen.applytojob.com/apply/v9MoFr2gnx/Summer-2023-DevOps-Intern?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,3.https://adelatech.com/adelatech-jobs/cloud-architect-and-devops-intern-apprentice/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,4.https://www.monster.com/job-openings/software-engineer-devops-summer-internship-weston-ma--9526b6fa-3381-4622-9d6f-5d023867f090?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,5.https://www.ziprecruiter.com/c/Bose-Corporation/Job/Security-DevOps-Engineering-Intern/-in-Framingham,MA?jid=a053022317016772&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic,6.https://ct.tarta.ai/j/14FJ14QBvf0LOA5Ejt3O1222-devops-engineer-intern-in-danbury-connecticut-at-experian?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic)-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
