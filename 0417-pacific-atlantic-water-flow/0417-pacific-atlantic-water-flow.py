import copy
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #do BFS visited array-x2 from pacific side and atlantic side; then take intersection
        
        def bfs(frontier, isVisited):
            while frontier:
                next=[]
                for nei in frontier:
                    i,j = nei
                    # print(nei)
                    if isVisited[i][j]: continue
                    isVisited[i][j]=True
    
                    if i>0 and heights[i-1][j]>=heights[i][j]: next.append((i-1,j))
                    if i<len(heights)-1 and heights[i+1][j]>=heights[i][j]: next.append((i+1,j))
                    if j>0 and heights[i][j-1]>=heights[i][j]: next.append((i,j-1))
                    if j<len(heights[0])-1 and heights[i][j+1]>=heights[i][j]: next.append((i,j+1))
                frontier=next
        
        canVisitP = copy.deepcopy([[False for _ in range(len(heights[0]))] for _ in range(len(heights))])
        canVisitA = copy.deepcopy(canVisitP)
        #sources for 'can visit from pacific ocean'
        sourcesForP= [(i,0) for i in range(len(heights))] + [(0,j) for j in range(len(heights[0]))]
        bfs(sourcesForP, canVisitP)
        m, n = len(heights)-1, len(heights[0])-1
        sourcesForA= [(m,i) for i in range(len(heights[0]))] + [(j,n) for j in range(len(heights))]
        bfs(sourcesForA, canVisitA)
        
        res=[]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if canVisitA[i][j] and canVisitP[i][j]: res.append([i, j])
        return res
                
        