class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        #at some point will need to identify whether there is apple on either side of cuts, we will have to use presums of apples
        rows,cols=len(pizza),len(pizza[0])
        #extra row and col at right and bottom as base conditions to calculate prefix sums
        preSum = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                preSum[i][j] = preSum[i+1][j] + preSum[i][j+1] - preSum[i+1][j+1] + (1 if pizza[i][j]=='A' else 0)
        
        @cache
        def dp(i,j,cutRemain):
            if preSum[i][j]==0:         #there is no apples beyond this point, hence stop the recursion by returning 0 possible ways
                return 0
            
            if cutRemain==0:
                return 1
            
            count=0
            for cutX in range(i+1, rows):
                if preSum[i][j] - preSum[cutX][j]>0:    #check if the upper part of the cut has apples or not, lower part will be taken care by the subproblem
                    count = (count + dp(cutX,j,cutRemain-1)) % (10**9+7)
            for cutY in range(j+1, cols):               #check if the left part of the cut has apples or not, right part will be taken care by the subproblem
                if preSum[i][j] - preSum[i][cutY]>0:
                    count = (count+ dp(i,cutY,cutRemain-1)) % (10**9+7)
                #the lower and right part will essentially become the upper and left part in the subsequent subproblems. if in any case or the last row/column doesnt have the apples the preSum check will make the function return 0, stopping the recursion branch further. if all condition satisfies and the cutRemain becomes zero, the recursion ends returning 1
            return count
        return dp(0,0,k-1)
    
        #status: correct; complete help(https://www.youtube.com/watch?time_continue=2447&v=RFyJMlpA-pY&embeds_euri=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dnumber%2Bof%2Bways%2Bof%2Bcutting%2Ba%2Bpizza%2Bneetcode%26newwindow%3D1%26rlz%3D1C5CHFA_enUS1021US1021%26sxsrf%3DAJOqlzWW&feature=emb_logo)
        #Analysis: Time O(rows*cols), Space O(rows*cols)
        #ref: 1/22/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day89/90Blind26/75,2q/dayDay8/10;0.absorber-x1pomo(6:00-6:30),1.predictiveIndexBehavioralAssesment;lastDate2/16/2023-x1pomo(6:30-7:00),3.;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day1/5-3q/day+searchOAQuestionsInReddit/csMajor,1.numberOfWaysOfCuttingPizzaTimed25Mins-x1pomo(7:00-7:30),2.implement-x2pomo(7:30-8:00),3.reachingPointsTimed25Mins-x1pomo(8:00-8:30),4.minimumIncrementToMakeArrayUniqueTimed25Mins-x1pomo(8:30-9:00),5.implement-x2pomo(9:00-10:00),6.01MatrixTimed25Mins-x1pomo(10:00-10:30),7.implement-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)=delayed=>1.predictiveIndexBehavioralAssesment;lastDate2/16/2023-x1pomo(7:30-8:00),3.;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day1/5-3q/day+searchOAQuestionsInReddit/csMajor,1.numberOfWaysOfCuttingPizzaTimed25Mins-x1pomo(8:00-8:30),2.implement-x2pomo(8:30-9:30),3.reachingPointsTimed25Mins-x1pomo(9:30-10:00),4.minimumIncrementToMakeArrayUniqueTimed25Mins-x1pomo(10:00-10:30),5.implement-x2pomo(10:30-11:00)=alter=>1.predictiveIndexBehavioralAssesment;lastDate2/16/2023-x1pomo(8:30-9:00),3.;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day1/5-3q/day+searchOAQuestionsInReddit/csMajor,1.numberOfWaysOfCuttingPizzaTimed25Mins-x1pomo(9:00-9:30),2.implement-x2pomo(9:30-10:30),3.reachingPointsTimed25Mins-x1pomo(10:30-11:00)

            
            
    