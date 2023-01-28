class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for aster in asteroids:
            while stack and stack[-1]>0 and aster<0:   #both are in opposite direction
                if stack[-1]<abs(aster):
                    stack.pop()
                elif stack[-1]>abs(aster):  #discard current aster
                    break
                elif stack[-1]==abs(aster):    
                    stack.pop()
                    break
            else:
                stack.append(aster)
        return stack