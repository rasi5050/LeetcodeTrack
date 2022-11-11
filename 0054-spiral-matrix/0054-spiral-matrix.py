class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #intuition:define boundaries and loop till boundary is hit
        #steps:
        #0.i=j==0, res=[]
        #1.left=0,top=0,right=len(matrix[0])-1, bottom=len(matrix)-1
        #2.while (left!=right and top!=bottom):
        #3.right movement, then down, left, up and loop
        #4.return res
        
        i=j=0
        left=top=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        res=[]
        totEle=(len(matrix))*(len(matrix[0]))
        while (len(res)<totEle):
            while (j<=right and len(res)<totEle):
                res.append(matrix[i][j])
                j+=1
            top+=1
            i+=1;j-=1
            while(i<=bottom and len(res)<totEle):
                res.append(matrix[i][j])
                i+=1
            right-=1
            j-=1;i-=1
            while(j>=left and len(res)<totEle):
                res.append(matrix[i][j])
                j-=1
            bottom-=1
            i-=1;j+=1
            while(i>=top and len(res)<totEle):
                res.append(matrix[i][j])
                i-=1
            left+=1
            j+=1;i+=1
        return res
    
    #status: correct took:25min+10Min
    #ref:11/10/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day35/36:do,1.1.SIG-60min(lastDate:6:46am PST on Friday, January 6th)-x2pomo(5:30-6:30),2.addQuestionsToGoogleDrive-x2pomo(6:30-7:30),3.spiralMatrixTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.rotateImageTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.validSudokuTimed25Mins-x1pomo(10:30-11:00),3.implement-x2pomo(11:00-12:00)=x13pomo(5:30-12:00)
