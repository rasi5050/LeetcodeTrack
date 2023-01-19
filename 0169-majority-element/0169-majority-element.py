class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #do Moore's voting algorithm
        #whenever the count of assumed majority goes to zero, majority is reset to next element
        count=0
        for n in nums:
            if count==0:           #resetting currMajority,because currMajority earlier cancelled out with equal count of minority
                currMajority=n
                count+=1
            elif currMajority==n:
                count+=1
            else:
                count-=1
        return currMajority  
    
    
    """
    #why this is working?
    say this is the array 
    [1,2,2,3,3,3,3,3,6]
    this is equivalent to writting
    [1,2,2,6] | 
    [3,3,3,3] | 3  ie. the counts of all other digits other than the majority element cancells out with count of majority element - 1, hence finally only majority element will win by atleast a count more
    
    algorithm counts for equal number of occurances of majority and minority elements, which will always cancel out except for the majority element
    """
    
    #status: correct
    #Analysis: Time O(n), Space O(1)
    #ref: 1/19/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day86/86C3Ai3QuestionsFromMostFrequentListOf7/10Day5/5+Blind16/75,2q/dayDay5/7;1.courseScheduleTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.groupAnagramsTimed25Mins-x1pomo(7:00-7:30),4.findAllAnagramsInAStringTimed25Mins-x1pomo(7:30-8:00),5.topKFrequentElementsTimed25Mins-x1pomo(8:00-8:30),6.majorityElementTimed25Mins-x1pomo(8:30-9:00),7.addBinaryTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.diameterOfABinaryTreeTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  

    
    