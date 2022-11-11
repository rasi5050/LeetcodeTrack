class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #intuition1: use hashmap to get [target-num] value
        # steps:
        #1.add array to hashMap, arrayElements as key, index as values
        #2.loop tru hashMap  ==> O(n)
        #3.for each curValue search for [target-curValue] available, return index(curValue,target-curValue)
        """ #correct code(hashMap 2 pass solution): commented for optimization
        hashMap={}
        for i,item in enumerate(nums):
            hashMap[item]=i
        for i,item in enumerate(nums):
            if (target-item) in hashMap and hashMap[target-item]!=i:
                return [i, hashMap[target-item]]
        """ #<<correctCodeEndsHere      
        #status: correct
        #missedOutEdgeCases:
        #1.resulting index is same as current index ==> added hashMap[target-item]!=i
        #2.2 instance of same number and if second number is in the result, result printed wrong==> automatically resolved by hashMap since there can be max of 2 instance of a number, the 2nd instance will be the updated in the hashMap and reverted.
        
        # ref:9/29/2022track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day9/10;useNotebookForGrind75Day3/7;stringDay7/3;buffer-;do;defineSteps,allCases.1.encodeDecodeStringsLogic-x2pomo,2.implementation-x1pomo,3.studyHashTable-x2pomo,4.do2Sum-x1pomo,5.ransomNoteLogic-x2pomo,6.implementation-x1pomo,7.absorber-x1pomo=x10pomo(7:30-12:30)==>3.studyHashTable-x2pomo,4.do2Sum-x1pomo,5.ransomNoteLogic-x2pomo,6.implementation-x1pomo,7.absorber-x3pomo=x9pomo(8:00-12:30)
        
        #optimization1: idea from leetcode solution; do hashMap in one pass, check compliment while inserting itself, it will find a compliment in the first number in a pair inserted, or surely in the 2nd number in the pair inserted.
        
        hashMap={}
        for i,item in enumerate(nums):
            if (target-item) in hashMap:
                return [i, hashMap[target-item]]
            hashMap[item]=i

        #status: correct
        
        
        

        