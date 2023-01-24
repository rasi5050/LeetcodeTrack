class Solution:
    def numTilings(self, n: int) -> int:
        #idea: after filling any possible postion represent the remaining empty spaces in top and bottom row.
        # (1,0) represents 1 square is free in top row, and 0 square is free in bottom row, hence when the index to the right most filled cell after adding domino or tromino reach hit the column maximum, the number of free top rows and bottom rows should be zero, that means they are completely filled.
        @cache
        def recurse(index, top, bottom):
            
            if index>n:   #the index has already passed the number of allowed columns
                return 0
            if index==n:  #at the time the index has reached the max columns there should not be any gaps in between, hence top==bottom==0
                return int(top==bottom==0)
            s=0
            if top==bottom==0:              #upto this point all cells are filled
                s+=recurse(index+1, 0,0)    #put a domino straight
                s+=recurse(index+2, 0,0)    #put two domino flat
                s+=recurse(index+1, 1,0)    #put a tromino shaped L
                s+=recurse(index+1, 0,1)    #put a tromino shaped L rotated 90degree
            
            if top==1 and bottom==0:        #this is the L tromino case
                s+=recurse(index+1, 0,1)    #put a domino flat on top row, then there is a new space on bottom row
                s+=recurse(index+2, 0,0)    #put a tromino shaped L rotated 180degrees, hence completely filled up to this point       
            
            if top==0 and bottom==1:   #this is the L rotated 90degrees tromino case
                s+=recurse(index+1, 1,0)    #put a domino flat on bottom row, then there is a new space on top row
                s+=recurse(index+2, 0,0)    #put a tromino shaped L rotated 270 degrees, hence completely filled upto this point
            return s % (10**9+7)
        return recurse(0,0,0)
    
        #status: correct; complete help in code and conceptualilzing (https://leetcode.com/problems/domino-and-tromino-tiling/discuss/2945421/Python-Simple-brute-force-with-cache-%3A-)), help in picturising(https://leetcode.com/problems/domino-and-tromino-tiling/discuss/2947428/Best-Python-Solution-Simple-DP-soln-No-complex-fullpartial-case-equation-needed)
        #Analysis: Time O(n), Space O(n)
        #ref: 1/24/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day91/92Blind29/75,2q/dayDay10/10;1.problems/number-of-times-binary-string-is-prefix-alignedTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day2/5-3q/day+searchOAQuestionsInReddit/csMajor,3.dominoAndTromilloTrailingTImed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.robotRoomCleaner-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.numberOfGoodLeafNodesPairsTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.3SumTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
