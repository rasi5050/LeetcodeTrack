class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        map={
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        res=[]
        def dfs(word,i):
            if len(word)==len(digits):
                res.append(word)
                return
            for c in map[digits[i]]:
                dfs(word+c, i+1)
        dfs('',0)
        return res if res!=[""] else []
    
    #status: correct
    #Analysis: Time O(4^n), Space O(4^n)
    #ref: 2/20/2023P2:track1-cpGrind75;Day114/114;1.containerWithMostWaterTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.letterCombinationsOfAPhoneNumberTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.wordSearch-x1pomo(8:00-8:30),6.implement-x2pomo(8:30-9:30),6.2/19/2023applyInternship-x6SWEFromGithubPage,(P2:applyInternship:1.belvedreTrading,2.cisco2From"message.rasi@gmail.com"),3.avanadeIntenship,4.cgiWithRubinRefferal(rubin.james@cgi.com)-x2pomo(9:30-10:30),7.applyInternshipFromGitHub-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

        