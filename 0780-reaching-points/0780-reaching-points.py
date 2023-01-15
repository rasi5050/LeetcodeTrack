class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """TLE
        def reach(sx,sy):
            if (sx,sy)==(tx,ty):
                return True
            if sx>tx or sy>ty:
                return False
            return reach(sx+sy,sy) or reach(sx, sy+sx)
        return reach(sx,sy)
        """
        #prune backwards(proccessed from bottom to up)
        """
        #cut branch to the second last
       (x,y)    //from corner2 reach (x,y)
        \
          \   <--(x+c*y, y)    //from corner1 reach this corner2; last corner
         /    <--(x, y+x)
       /      <--(x, y+ 2*x)
     /        <--(x, y+ c*x)
      \
        \  from (tx,ty) reach this corner1
       /
     /
    (tx,ty)
    """
        #cut till last corner
        while tx>sx and ty>sy:    
            tx,ty=tx%ty, ty%tx
        #after this we might be at the (sx,sy) or one straight branch away from (sx,sy)
        """
        conditions:
            reached the target  (sx,sy) ie. sx==tx and sy==ty
            one straight branch to the left  (sx,sy+k*sx)  ie. sx==tx and (ty-sy)%sx==0
            one straight branch to the right (sx+k*sy, sy)  ie. sy==ty and (tx-sx)%sy==0
        """
        return sy==ty and tx>=sx and (tx-sx)%sy==0 or sx==tx and ty>=sy and (ty-sy)%sx==0