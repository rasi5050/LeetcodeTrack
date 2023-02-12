class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix), len(matrix[0])
        left,right,top,bottom=-1,len(matrix[0]),-1,len(matrix)
        res=[]
        (i,j)=(0,0)
        while top<i<bottom and left<j<right:
            while j<right and (top!=bottom-1 and left!=right-1):   #traverse right
                res.append(matrix[i][j])
                (i,j)=(i,j+1)
            (i,j)=(i+1,j-1)
            top+=1
            while i<bottom and (top!=bottom-1 and left!=right-1):   #traverse down
                res.append(matrix[i][j])
                (i,j)=(i+1,j)
            (i,j)=(i-1,j-1)    
            right-=1
            while j>left and (top!=bottom-1 and left!=right-1):   #traverse left
                res.append(matrix[i][j])
                (i,j)=(i, j-1)
            (i,j)=(i-1, j+1)
            bottom-=1
            while i>top and (top!=bottom-1 and left!=right-1):   #traverse up
                res.append(matrix[i][j])
                (i,j)=(i-1,j)
            (i,j)=(i+1,j+1)
            left+=1
        return res 
    
    #synopsis: fix 4 boundaries top, bottom, left, right. then iterete to right->down->left->up using (i,j)
    # when a direction is complete set pointer a place back then to the next possible candidate. edge case is a single row or column, it can be identified using marking visited elements as '#' or checking the (top!=bottom-1)
    #status: correct; took 40mins to complete
    #Analsysis: Time O(m*n), Space O(m*n)
    #ref: 2/12/2023P2:track1-cpGrind75;Day107/108;doLeetcodeBlind75-3q/day-21/45Q:completeOn2/15/2023-Day15/15,collateQuestionPatternIntoCategoriesAndTemplate-Day6/5:(addWordDescriptionOnceProblemIsSolvedDay5/4),1.sprialMatrixTimed25Mins-x1pomo(6:30-7:00),2.implement-x2pomo(7:00-8:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)shortened(6:30-8:00)
