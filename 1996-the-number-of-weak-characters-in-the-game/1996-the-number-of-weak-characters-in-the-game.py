class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0],-x[1]))
        #now if we traverse from properties[::-1], attack values are already sorted, do dont have to care, only have to care if reverse sorted defence values are breaking the constraint
        # ie. if a defense value is lower than the previous maximum
        
        currMax=0
        weakCounter=0
        for _,defense in properties[::-1]:
            if defense<currMax:
                weakCounter+=1
            currMax=max(currMax,defense)
        return weakCounter
        
    
    
    
