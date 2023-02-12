class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix), len(matrix[0])
        left,right,top,bottom=-1,len(matrix[0]),-1,len(matrix)
        res=[]
        (i,j)=(0,0)
        while top<i<bottom or left<j<right:
            while j<right and matrix[i][j]!='#':   #traverse right
                res.append(matrix[i][j])
                matrix[i][j]='#'
                (i,j)=(i,j+1)
            (i,j)=(i+1,j-1)
            top+=1
            while i<bottom and matrix[i][j]!='#':   #traverse down
                res.append(matrix[i][j])
                matrix[i][j]='#'
                (i,j)=(i+1,j)
            (i,j)=(i-1,j-1)    
            right-=1
            while j>left and matrix[i][j]!='#':   #traverse left
                res.append(matrix[i][j])
                matrix[i][j]='#'
                (i,j)=(i, j-1)
            (i,j)=(i-1, j+1)
            bottom-=1
            while i>top and matrix[i][j]!='#':   #traverse up
                res.append(matrix[i][j])
                matrix[i][j]='#'
                (i,j)=(i-1,j)
            (i,j)=(i+1,j+1)
            left+=1
        return res 