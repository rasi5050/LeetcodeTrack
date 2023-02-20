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
        