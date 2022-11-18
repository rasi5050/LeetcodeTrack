class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #intuition: oscilatting pointer 
        rows= ["" for i in range(numRows)]
        oscilate=0
        index=0
        while index<len(s):
            while oscilate<numRows and index<len(s):
                rows[oscilate]+=(s[index])    #time O(1), because string append of 1 char
                oscilate+=1
                index+=1
            oscilate-=2
            while oscilate>0 and index<len(s):
                rows[oscilate]+=(s[index])
                oscilate-=1
                index+=1
        return "".join(rows)
        #status: correct
        #analysis: Time O(n), since each char is processed once
        #Space O(n), since each element is only stored once in any of the strings
        #ref:11/18/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day41/42:(P1:doPaypalLeetcodeQuestion2/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,1.medianOfTwoSortedArraysTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.zigzagConversionTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.trappingRainWaterTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.absorber-x1pomo(10:00-10:30)=x10pomo(5:30-10:30)==>11/18/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day41/42:(P1:doPaypalLeetcodeQuestion2/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,1.mergeTwoSortedArrays-implement-x2pomo(7:00-8:00),2.zigzagConversionTimed25Mins-x1pomo(8:00-8:30),3.implement-x2pomo(8:30-9:30),4.trappingRainWaterTimed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.bestTimeToBuyAndSellStocksTimed25Mins-x1pomo(11:00-11:30),8.implement-x2pomo(11:30-12:30)=x11pomo(7:00-12:30)
