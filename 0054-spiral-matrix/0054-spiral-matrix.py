class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix), len(matrix[0])
        left,right,top,bottom=-1,len(matrix[0]),-1,len(matrix)
        res=[]
        (i,j)=(0,0)
        while top<i<bottom and left<j<right:
            while j<right and (top!=bottom-1 and left!=right-1):   #traverse right
                print('hit1', matrix[i][j], (i,j))
                res.append(matrix[i][j])
                (i,j)=(i,j+1)
            (i,j)=(i+1,j-1)
            top+=1
            while i<bottom and (top!=bottom-1 and left!=right-1):   #traverse down
                print('hit2', matrix[i][j], (i,j))
                res.append(matrix[i][j])
                (i,j)=(i+1,j)
            (i,j)=(i-1,j-1)    
            right-=1
            while j>left and (top!=bottom-1 and left!=right-1):   #traverse left
                print('hit3', matrix[i][j], (i,j))
                res.append(matrix[i][j])
                (i,j)=(i, j-1)
            (i,j)=(i-1, j+1)
            bottom-=1
            while i>top and (top!=bottom-1 and left!=right-1):   #traverse up
                print('hit4', matrix[i][j], (i,j))
                res.append(matrix[i][j])
                (i,j)=(i-1,j)
            (i,j)=(i+1,j+1)
            left+=1
        return res 