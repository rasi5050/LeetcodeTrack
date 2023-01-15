class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """TLE
        def reach(sx,sy):
            if (sx,sy)==(tx,ty):
                return True
            if sx>tx or sy>ty:
                return False
            return reach(sx+sy,sy) or reach(sx, sy+sx)
        return reach(sx,sy)
        """
        #prune backwards(proccessed from bottom to up)
        """
        #cut branch to the second last
       (x,y)    //from corner2 reach (x,y)
        \
          \   <--(x+c*y, y)    //from corner1 reach this corner2; last corner
         /    <--(x, y+x)
       /      <--(x, y+ 2*x)
     /        <--(x, y+ c*x)
      \
        \  from (tx,ty) reach this corner1
       /
     /
    (tx,ty)
    """
        #cut till last corner
        while tx>sx and ty>sy:    
            tx,ty=tx%ty, ty%tx
        #after this we might be at the (sx,sy) or one straight branch away from (sx,sy)
        """
        conditions:
            reached the target  (sx,sy) ie. sx==tx and sy==ty
            one straight branch to the left  (sx,sy+k*sx)  ie. sx==tx and (ty-sy)%sx==0
            one straight branch to the right (sx+k*sy, sy)  ie. sy==ty and (tx-sx)%sy==0
        """
        return sy==ty and tx>=sx and (tx-sx)%sy==0 or sx==tx and ty>=sy and (ty-sy)%sx==0
    
    #status: success; idea from (https://leetcode.com/problems/reaching-points/discuss/114856/JavaC%2B%2BPython-Modulo-from-the-End)
    #Analysis: Time O(log(min(tx,ty))), Space O(1)
    #ref: 1/15/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day82/82C3Ai3QuestionsFromMostFrequentListOf0/10Day2/5+Blind75WeekOne0/14q,2q/dayDay2/7-,1.countVowelsPermutationTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.reachingPointsTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.longestArithmeticSubsequenceTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),Blind753q/Day,7.2SumTimed25Mins-x1pomo(10:00-10:30),8.validParenthesesTImed25Mins-x1pomo(10:30-11:00),9.mergeTwoSortedListsTimed25Mins-x1pomo(11:00-11:30=x12pomo(5:30-11:30)  
