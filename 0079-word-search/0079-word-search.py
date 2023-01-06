class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #do 2x2 case
        """working code; TLE; brute force, so add memoization
        visited = set()
        def dfs(x,y,curWord, word):
            #another base condition to chech bounds and visited
            print(visited)
            print(curWord)
            if curWord==word:
                return True
            
            output=False
            visited.add((x,y))
            
            if x>0 and (x-1,y) not in visited: output|=dfs(x-1,y,curWord+board[x-1][y], word)
            if x<len(board)-1 and (x+1,y) not in visited: output|=dfs(x+1,y,curWord+board[x+1][y], word)
            if y>0 and (x,y-1) not in visited: output|=dfs(x,y-1,curWord+board[x][y-1], word)
            if y<len(board[0])-1 and (x,y+1) not in visited: output|=dfs(x,y+1,curWord+board[x][y+1], word)
                
            visited.remove((x,y))
            return output
            
            
        #call for all occurances of starting letter of word
        for r in range(len(board)):
            for c in range(len(board[0])):
                visited.add((r,c))
                if board[r][c]==word[0] and dfs(r,c, word[0], word)==True: return True
                visited.remove((r,c))
        return False
        """
        """working code; commented to increase efficiency
        visited = set()
        def dfs(x,y,curWord, word, i):
            #another base condition to chech bounds and visited
            # print(visited)
            # print(curWord)
            if curWord==word:
                return True
            if len(curWord)>=len(word):
                return False
            output=False
            visited.add((x,y))
            
            if x>0 and (x-1,y) not in visited and word[i]==board[x-1][y]: output|=dfs(x-1,y,curWord+board[x-1][y], word, i+1)
            if x<len(board)-1 and (x+1,y) not in visited and word[i]==board[x+1][y]: output|=dfs(x+1,y,curWord+board[x+1][y], word, i+1)
            if y>0 and (x,y-1) not in visited and word[i]==board[x][y-1]: output|=dfs(x,y-1,curWord+board[x][y-1], word, i+1)
            if y<len(board[0])-1 and (x,y+1) not in visited and word[i]==board[x][y+1]: output|=dfs(x,y+1,curWord+board[x][y+1], word, i+1)
                
            visited.remove((x,y))
            return output
            
            
        #call for all occurances of starting letter of word
        for r in range(len(board)):
            for c in range(len(board[0])):
                # visited.add((r,c))
                if board[r][c]==word[0] and dfs(r,c, word[0], word,i:=1)==True: return True
                # visited.remove((r,c))
        return False
        """
        #working; now increase efficiency
        
        #adding extra cases for efficiency
        #case1. if number of words in boards in not enough for required word
        m,n=len(board), len(board[0])
        
        if (m*n)<len(word): return False
        
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
            # temp = board[r][c]
            # board[r][c] = '#'
            
            res = dfs(x+1, y, i+1) or dfs(x-1, y, i+1) or dfs(x, y-1, i+1) or dfs(x, y+1, i+1)
            # board[r][c] = temp
            visited.remove((x,y))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c, 0): return True
        return False
            
            
            
        
            