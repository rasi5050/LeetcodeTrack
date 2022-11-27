class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        #cummulative reverse sum of shifts
        cumPrev=0
        s=list(s)
        for i in reversed(range(len(shifts))):
            shifts[i]+=cumPrev
            cumPrev=shifts[i]
            s[i]=chr((ord(s[i])-97+shifts[i])%26+97)
        return ''.join(s)
        #status: correct
        #analysis: Time: O(n), Space: O(1), only 1 variable
        #ref:11/27/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day50/50:1.(P1:doPaypalLeetcodeQuestion7/5),2.shiftingLettersTimed25Mins-x1pomo(14:30-15:00),3.implement-x2pomo(15:00-16:00),4.firstUniqueCharecterInStringTimed25Mins-x1pomo(16:00-16:30),5.repeat;pairOfSongsDivBy60Timed25Mins-x1pomo(16:30-17:00),6.repeat;minimumAbsoluteDifferenceTimed25Mins-x1pomo(17:00-17:30),7.repeat;lruCacheTimed25Mins-x1pomo(17:30-18:00),8.implement-x1pomo(18:00-18:30)=x9pomo(14:00-18:30)

        
