class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        #do normal approach
        """TLE
        @cache
        def recurse(sx,sy):
            if sx>tx or sy>ty:
                return False
            if sx==tx and sy==ty:
                return True
            return recurse(sx+sy, sy) or recurse(sx, sy+sx)
        return recurse(sx,sy)
        """
        #this is not efficient pruning as it lead to all possible branches from root to all leaf nodes, which is O(2^n)
        #instead do reverse pruning, starting from leaf to root, which will have only one path
        
        #do reverse pruning. this is like going up the zip zag path until 2nd last zig zag
        
        #say we have (a,b), one of the straight path is (a+b, b)-> (a+2b, b)->(a+3b, b)->(a+4b, b), if target=(a+4b, b) and the root=(a,b) , if we were to find the target to root path we would go from (a+4b, b)->(a+4b-b,b)->(a+4b-2b,b)->(a+4b-3b,b)->(a+4b-4b,b)
        """
        hence we can conclude (a+4b)%b will give us (a)
        simmilarly (a, b+4a), on (b+4a)%a will give b
        this is the case for a straight line , hence we loop process it till all the straight lines in zig zag. this will lead to (0,0)
        
        however we have specific source, so we stop 1 step below the source and manually decrement to the source.
        
        the cases would be 
        either one of the coordinates as same as of source ==> have to check for correctness
        both of them are same as of source  => correct
        either one of them or both have gone beyond the source ==>invalid case
        """
        
        while sx<tx and sy<ty:
            tx,ty=tx%ty,ty%tx
        # cases
        if sx==tx and ty>=sy and (ty-sy)%sx==0: return True
        if sy==ty and tx>=sx and (tx-sx)%sy==0: return True
        return False
    
        #status: correct
        #Analysis: Time(log(max(tx,ty))), Space O(1)
        #ref: 1/22/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day89/90Blind26/75,2q/dayDay8/10;0.absorber-x1pomo(6:00-6:30),1.predictiveIndexBehavioralAssesment;lastDate2/16/2023-x1pomo(6:30-7:00),3.;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day1/5-3q/day+searchOAQuestionsInReddit/csMajor,1.numberOfWaysOfCuttingPizzaTimed25Mins-x1pomo(7:00-7:30),2.implement-x2pomo(7:30-8:00),3.reachingPointsTimed25Mins-x1pomo(8:00-8:30),4.minimumIncrementToMakeArrayUniqueTimed25Mins-x1pomo(8:30-9:00),5.implement-x2pomo(9:00-10:00),6.01MatrixTimed25Mins-x1pomo(10:00-10:30),7.implement-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)=delayed=>1.predictiveIndexBehavioralAssesment;lastDate2/16/2023-x1pomo(7:30-8:00),3.;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day1/5-3q/day+searchOAQuestionsInReddit/csMajor,1.numberOfWaysOfCuttingPizzaTimed25Mins-x1pomo(8:00-8:30),2.implement-x2pomo(8:30-9:30),3.reachingPointsTimed25Mins-x1pomo(9:30-10:00),4.minimumIncrementToMakeArrayUniqueTimed25Mins-x1pomo(10:00-10:30),5.implement-x2pomo(10:30-11:00)=alter=>1.predictiveIndexBehavioralAssesment;lastDate2/16/2023-x1pomo(8:30-9:00),3.;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day1/5-3q/day+searchOAQuestionsInReddit/csMajor,1.numberOfWaysOfCuttingPizzaTimed25Mins-x1pomo(9:00-9:30),2.implement-x2pomo(9:30-10:30),3.reachingPointsTimed25Mins-x1pomo(10:30-11:00)

        