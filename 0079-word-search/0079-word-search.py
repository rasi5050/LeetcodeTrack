class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board), len(board[0])
        visited=set()
        def dfs(i,j,k):
            if k==len(word):
                return True
            if i<0 or j<0 or i>m-1 or j>n-1 or board[i][j]!=word[k] or (i,j) in visited:
                return False      
            visited.add((i,j))
            res= dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1)
            visited.remove((i,j))
            return res
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0)==True:
                    return True
        return False
    
    #status: correct
    #Analysis: Time O(m*n), Space O(m*n)
    #ref: 2/20/2023P2:track1-cpGrind75;Day114/114;1.containerWithMostWaterTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.letterCombinationsOfAPhoneNumberTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.wordSearch-x1pomo(8:00-8:30),6.implement-x2pomo(8:30-9:30),6.2/19/2023applyInternship-x6SWEFromGithubPage,(P2:applyInternship:1.belvedreTrading,2.cisco2From"message.rasi@gmail.com"),3.avanadeIntenship,4.cgiWithRubinRefferal(rubin.james@cgi.com)-x2pomo(9:30-10:30),7.applyInternshipFromGitHub-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

        