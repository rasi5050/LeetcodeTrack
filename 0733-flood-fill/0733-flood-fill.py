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
    
    #status: correct
    #Analysis: Time O(n); atmost each elements in the matrix will be visited
    #Space O(1); inplace
    #ref: 1/15/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day82/82C3Ai3QuestionsFromMostFrequentListOf0/10Day2/5+Blind75WeekOne0/14q,2q/dayDay2/7-,1.binarySearchTimed25Mins-x1pomo(18:30-19:00),2.implement-x1pomo(19:00-19:30),3.floodFillTimed25Mins-x1pomo(19:30-20:00),4.implement-x1pomo(20:00-20:30)=x4pomo(18:30-20:30)
