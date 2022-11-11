class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                elif (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in boxes[(i//3)*3 + j//3]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i//3)*3 + j//3].add(board[i][j])
        return True
    
    #status: correct:
    #ref:11/10/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day35/36:do,1.1.SIG-60min(lastDate:6:46am PST on Friday, January 6th)-x2pomo(5:30-6:30),2.addQuestionsToGoogleDrive-x2pomo(6:30-7:30),3.spiralMatrixTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.rotateImageTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.validSudokuTimed25Mins-x1pomo(10:30-11:00),3.implement-x2pomo(11:00-12:00)=x13pomo(5:30-12:00)
    #analysis: Time O(9*9)=O(1)
    #          Space O(9*9)=O(1)