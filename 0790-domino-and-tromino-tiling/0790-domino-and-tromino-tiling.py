class Solution:
    def numTilings(self, n: int) -> int:
        #idea: after filling any possible postion represent the remaining empty spaces in top and bottom row.
        # (1,0) represents 1 square is free in top row, and 0 square is free in bottom row, hence when the index to the right most filled cell after adding domino or tromino reach hit the column maximum, the number of free top rows and bottom rows should be zero, that means they are completely filled.
        @cache
        def recurse(index, top, bottom):
            
            if index>n:   #the index has already passed the number of allowed columns
                return 0
            if index==n:  #at the time the index has reached the max columns there should not be any gaps in between, hence top==bottom==0
                return int(top==bottom==0)
            s=0
            if top==bottom==0:              #upto this point all cells are filled
                s+=recurse(index+1, 0,0)    #put a domino straight
                s+=recurse(index+2, 0,0)    #put two domino flat
                s+=recurse(index+1, 1,0)    #put a tromino shaped L
                s+=recurse(index+1, 0,1)    #put a tromino shaped L rotated 90degree
            
            if top==1 and bottom==0:        #this is the L tromino case
                s+=recurse(index+1, 0,1)    #put a domino flat on top row, then there is a new space on bottom row
                s+=recurse(index+2, 0,0)    #put a tromino shaped L rotated 180degrees, hence completely filled up to this point       
            
            if top==0 and bottom==1:   #this is the L rotated 90degrees tromino case
                s+=recurse(index+1, 1,0)    #put a domino flat on bottom row, then there is a new space on top row
                s+=recurse(index+2, 0,0)    #put a tromino shaped L rotated 270 degrees, hence completely filled upto this point
            return s % (10**9+7)
        return recurse(0,0,0)
    
        #status: correct; complete help