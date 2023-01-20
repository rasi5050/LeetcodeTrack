class Solution:
    def countVowelPermutation(self, n: int) -> int:
        map={
            '.': ['a','e','i','o','u'],   #added as single point dummy node to connect all nodes
            'a': ['e'],
            'e': ['a','i'],
            'i': ['a','e','o','u'],
            'o': ['i','u'],
            'u': ['a']
        }
        memo={}   
        def recurse(i,c):
            if (i,c) in memo: return memo[(i,c)]
            if i==n:
                return 1
            if i>n:
                return 0
            count=0
            for each in map[c]:
                count=(count+recurse(i+1, each)) % 1000000007
            memo[(i,c)]=count
            return count
        return recurse(0,'.')
    
    #status: correct
    #Analysis: Time O(5^n), Space O(5^n)
    #ref: 1/20/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day87/88C3Ai3QuestionsFromMostFrequentListOf10/10Day6/5+Blind20/75,2q/dayDay6/7; 1.Count Vowels PermutationTimed25Mins-x1pomo(6:00-6:30),2.reachingPointsTimed25Mins-x1pomo(6:30-7:00),3.longestArithmeticSequenceTimed25Mins-x1pomo(7:00-7:30),3.diameterOfABinaryTreeTimed25Mins-x1pomo(7:30-8:00),4.implement-x1pomo(8:00-8:30),5.middleOfLinkedListTimed25Mins-x1pomo(8:30-9:00),6.maximumDepthOfBinaryTreeTimed25Mins-x1pomo(9:00-9:30),7.containsDuplicateTimed25Mins-x1pomo(9:30-10:00),8.maximumSubarrayTimed25Mins-x1pom(10:00-10:30),9.absorber-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  
