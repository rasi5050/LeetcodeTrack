class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        sourceColor=image[sr][sc]
        visited=set()
        def dfs(x,y):
            #base conditions
            if x<0 or y<0 or x>len(image)-1 or y>len(image[0])-1 or image[x][y]!=sourceColor or (x,y) in visited:
                return
            
            image[x][y]=color
            visited.add((x,y))
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        dfs(sr,sc)
        return image