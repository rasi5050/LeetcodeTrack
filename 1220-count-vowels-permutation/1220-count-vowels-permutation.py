class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """working code; commented to try alternate 
        map={
            '.': ['a','e','i','o','u'],
            'a': ['e'],
            'e': ['a','i'],
            'i': ['a','e','o','u'],
            'o': ['i','u'],
            'u': ['a'],
        }
        memo={}
        def recurse(s,cur):
            if (s,cur) in memo:
                return memo[(s,cur)]
            if s==n:
                return 1
            memo[(s,cur)]=0
            for mapping in map[cur]:
                memo[(s,cur)] = (memo[(s,cur)]+recurse(s+1, mapping))%1000000007
            return memo[(s,cur)]
        return recurse(0,'.')
    """
    #status: correct
    #Analysis: Time O(number of leaves of tree)=5+5*5+5*5*5+...=5^n
    #Space O(5^n)
    #ref: 1/15/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day82/82C3Ai3QuestionsFromMostFrequentListOf0/10Day2/5+Blind75WeekOne0/14q,2q/dayDay2/7-,1.countVowelsPermutationTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.reachingPointsTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.longestArithmeticSubsequenceTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),Blind753q/Day,7.2SumTimed25Mins-x1pomo(10:00-10:30),8.validParenthesesTImed25Mins-x1pomo(10:30-11:00),9.mergeTwoSortedListsTimed25Mins-x1pomo(11:00-11:30=x12pomo(5:30-11:30)  

        #concise code
        map={
            '.':['a','e','i','o','u'],
            'a':['e'],
            'e':['a','i'],
            'i':['a','e','o','u'],
            'o':['i','u'],
            'u':['a']
        }
        @lru_cache(None)
        def recurse(s,cur):
            if s==n:
                return 1
            count=0
            for mapping in map[cur]:
                count=(count+recurse(s+1, mapping))%1000000007
            return count
        return recurse(0,'.')
            
            