class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """working code; inefficient; commented to try alter
        res=set()
        comb=[]
        def dfs(comb,combSum):
            if combSum==target:
                res.add(tuple(sorted(comb)))
            if combSum>target:
                return
            for candidate in candidates:
                comb.append(candidate)
                dfs(comb, combSum+candidate)
                comb.pop()
        dfs([],0)
        return res
        """
        #status: correct
        #Analysis: Time O(n log n), Space O(n)
        #ref:2/1/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day99/100Blind42/75;doLeetcodeBlind75-3q/day-12/45Q:completeOn2/15/2023-Day5/15:1.combinationSumTImed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.permutationsTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.mergeIntervalsTimed25Mins-x1pomo(8:00-8:30),6.homeWork:DBMS:q6-x1pomo(8:30-9:00),7.homeWork:DBMS:q7-x1pomo(9:00-9:30),8.homeWork:DBMS:q8-x1pomo(9:30-10:00),9.absorber-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
        res=[]
        def dfs(i, cur, total):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            
            dfs(i+1, cur, total)
        
        
        dfs(0, [], 0)
        return res