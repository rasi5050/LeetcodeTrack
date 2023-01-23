class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        #do from all zeroes to as single dummy node to ones
        frontier=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    frontier.append((i,j))
        res=[[0]*len(mat[0]) for _ in range(len(mat))]
        level=0
        visited=set()
        while frontier:
            next=[]
            for x,y in frontier:
                if not(x<0 or y<0 or x>len(mat)-1 or y>len(mat[0])-1 or (x,y) in visited):
                    if mat[x][y]==1:
                        res[x][y]=level
                        # continue  #earlier thought, it should end when it sees a 1, but found that it should not because there could be 1 which can be only reached through only ones
                    visited.add((x,y))
                    next.append((x-1,y))
                    next.append((x+1,y))
                    next.append((x,y-1))
                    next.append((x,y+1))
            frontier=next
            level+=1
        return res