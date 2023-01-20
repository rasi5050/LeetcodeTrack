class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        while sx<tx and sy<ty:
            tx,ty = tx%ty, ty%tx    
            #here tx=tx%ty essentially says how many times ty was added before to tx contiguously
            
        print(tx, ty)
        if tx==sx and ty>=sy: return (ty-sy)%sx==0
        if ty==sy and tx>=sx: return (tx-sx)%sy==0
    