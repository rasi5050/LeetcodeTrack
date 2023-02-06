class Solution:
    def countVowelStrings(self, n: int) -> int:
        """working code;commented for alter
        map={
            '.': ['a','e','i','o','u'],
            'a': ['a','e','i','o','u'],
            'e': ['e','i','o','u'],
            'i': ['i','o','u'],
            'o': ['o','u'],
            'u': ['u']
        }
        @cache
        def dfs(curr, l):
            if l==n:
                return 1        
            count=0
            for c in map[curr]:
                count+=dfs(c, 1+l)
            return count
        return dfs('.', 0)
        """  
    #status: correct
    #Analysis: Time O(5^n), Space O(1)
    #ref: 2/6/2023P2:track1-cpGrind75;Day102/102;doLeetcodeBlind75-3q/day-16/45Q:completeOn2/15/2023-Day10/15:prepareTiktokDevOpsIntenseFocusDay3/7;1.(https://leetcode.com/problems/design-a-stack-with-increment-operation/)-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.(https://leetcode.com/discuss/interview-question/1263982/thomson-reuters-oa-circular-printer)-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.(https://leetcode.com/problems/count-sorted-vowel-strings/discuss/1021180/python-start-and-bars-explained)-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.absorber-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
    
    #help(https://leetcode.com/problems/count-sorted-vowel-strings/discuss/1021180/python-start-and-bars-explained)
    
        return ((n+4)*(n+3)*(n+2)*(n+1))//(4*3*2*1)
    #status: correct; didnot understand; help(https://leetcode.com/problems/count-sorted-vowel-strings/discuss/1021180/python-start-and-bars-explained)
    #Analysis: Time O(1), Space O(1)
    #ref: 2/6/2023P2:track1-cpGrind75;Day102/102;doLeetcodeBlind75-3q/day-16/45Q:completeOn2/15/2023-Day10/15:prepareTiktokDevOpsIntenseFocusDay3/7;1.(https://leetcode.com/problems/design-a-stack-with-increment-operation/)-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.(https://leetcode.com/discuss/interview-question/1263982/thomson-reuters-oa-circular-printer)-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.(https://leetcode.com/problems/count-sorted-vowel-strings/discuss/1021180/python-start-and-bars-explained)-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.absorber-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

    