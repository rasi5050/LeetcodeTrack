import sys
sys.setrecursionlimit(550000)

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        """TLE
        def recurse(x,y):
            if (x,y) == (tx,ty):
                return True
            if x>tx or y>ty:
                return False
            return recurse(x, x+y) or recurse(x+y, y)
        return recurse(sx,sy)
        """
        
        while (sx < tx and sy < ty):  
            #we are trying to reduce tx, ty to sx,sy
            if (tx<ty):   #we should do (tx, ty-tx)
                ty%=tx
            else:
                tx%=ty
                
        if sx==tx and sy<=ty and (ty-sy)%sx==0:
            return True
        return sy==ty and sx<=tx and (tx-sx)%sy==0
                
            
