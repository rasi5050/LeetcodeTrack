class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        #do normal approach
        """TLE
        @cache
        def recurse(sx,sy):
            if sx>tx or sy>ty:
                return False
            if sx==tx and sy==ty:
                return True
            return recurse(sx+sy, sy) or recurse(sx, sy+sx)
        return recurse(sx,sy)
        """
        #this is not efficient pruning as it lead to all possible branches from root to all leaf nodes, which is O(2^n)
        #instead do reverse pruning, starting from leaf to root, which will have only one path
        
        #do reverse pruning. this is like going up the zip zag path until 2nd last zig zag
        
        #say we have (a,b), one of the straight path is (a+b, b)-> (a+2b, b)->(a+3b, b)->(a+4b, b), if target=(a+4b, b) and the root=(a,b) , if we were to find the target to root path we would go from (a+4b, b)->(a+4b-b,b)->(a+4b-2b,b)->(a+4b-3b,b)->(a+4b-4b,b)
        """
        hence we can conclude (a+4b)%b will give us (a)
        simmilarly (a, b+4a), on (b+4a)%a will give b
        this is the case for a straight line , hence we loop process it till all the straight lines in zig zag. this will lead to (0,0)
        
        however we have specific source, so we stop 1 step below the source and manually decrement to the source.
        
        the cases would be 
        either one of the coordinates as same as of source ==> have to check for correctness
        both of them are same as of source  => correct
        either one of them or both have gone beyond the source ==>invalid case
        """
        
        while sx<tx and sy<ty:
            tx,ty=tx%ty,ty%tx
        # cases
        if sx==tx and ty>=sy and (ty-sy)%sx==0: return True
        if sy==ty and tx>=sx and (tx-sx)%sy==0: return True
        return False