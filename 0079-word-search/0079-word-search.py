class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board), len(board[0])
	   #fix1 for TLE; if there are not enough letters on board even to make the word
        if (m*n)<len(word): return False
        
		#fix2 for TLE; if first letter of word has more occurances than the last letter of word, then start searching in reverse order of word (intuition: start pruning with less branches)
        from collections import Counter
        word_freq = Counter(word)
        if word_freq[word[0]]>word_freq[word[-1]]:
            word=word[::-1]
        
        visited=set()
        def dfs(x, y , i):   
            if i==len(word):
                return True
            if (x<0 or y<0 or 
            x>len(board)-1 or 
            y>len(board[0])-1 or 
            board[x][y]!=word[i] or
            (x,y) in visited):
                return False
            
            visited.add((x,y))
            
            res = dfs(x+1, y, i+1) or dfs(x-1, y, i+1) or dfs(x, y-1, i+1) or dfs(x, y+1, i+1)
            # board[r][c] = temp
            visited.remove((x,y))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c, 0): return True
        return False
            
            
            
        
            