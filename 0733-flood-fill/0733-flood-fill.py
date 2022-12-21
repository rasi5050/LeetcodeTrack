class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color : return image      
        def dfs(i, j):
            nonlocal image
            nonlocal color
            nonlocal fromColor
            if i<0 or j<0 or i>len(image)-1 or j>len(image[0])-1 or image[i][j]!=fromColor:
                return 
            image[i][j]=color
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        fromColor = image[sr][sc]    
        dfs(sr, sc)    
        return image