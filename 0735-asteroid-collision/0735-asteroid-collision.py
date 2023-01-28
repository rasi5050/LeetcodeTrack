class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for aster in asteroids:
            notInsert=False
            while stack and stack[-1]*aster<0 and not(stack[-1]<0 and aster>0):  #opposite direction, hit hit
                if stack[-1]<abs(aster):
                    stack.pop()
                elif stack[-1]==abs(aster):
                    stack.pop()
                    notInsert=True
                    break
                else:
                    notInsert=True
                    break
            if not notInsert: stack.append(aster)
        return stack    
        