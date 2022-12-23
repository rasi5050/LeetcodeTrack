import copy
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #do BFS visited array-x2 from pacific side and atlantic side; then take intersection
        
        def bfs(frontier, isVisited):
            while frontier:
                next=[]
                for nei in frontier:
                    i,j = nei
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
        #status: correct; @Rasi's code ;translated from c++ bfs solution (https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/1126938/Short-and-Easy-w-Explanation-and-diagrams-or-Simple-Graph-traversals-DFS-and-BFS)
        #Analyis: Time O(mn);  cells can be visited by both atlantic and pacific oceans
        #Space: O(3*mn)=O(mn); visited is kept track in different matrix
        #ref: 12/23/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day59/60,1.cloneGraphTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.pacificAtlanticWaterFlowTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.courseScheduleTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.studyHeap-x1pomo(10:00-10:30),8.mergeKSortedListsTimed25Mins-x1pomo(10:30-11:00),9.implement-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)
