class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=n=len(matrix)-1+2
        i=j=-1
        for _ in range((m+1)//2):
            i+=1;j+=1
            m-=2;n-=2
            for k in range(m):
                matrix[i][j+k],matrix[i+k][j+n],matrix[i+m][j+n-k],matrix[i+m-k][j]=matrix[i+m-k][j],matrix[i][j+k],matrix[i+k][j+n],matrix[i+m][j+n-k]
        #status: correct
        #ref:11/10/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day35/36:do,1.1.SIG-60min(lastDate:6:46am PST on Friday, January 6th)-x2pomo(5:30-6:30),2.addQuestionsToGoogleDrive-x2pomo(6:30-7:30),3.spiralMatrixTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.rotateImageTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.validSudokuTimed25Mins-x1pomo(10:30-11:00),3.implement-x2pomo(11:00-12:00)=x13pomo(5:30-12:00)
        #analysis: Time O(m*n) Space O(1)