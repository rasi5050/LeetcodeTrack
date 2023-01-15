class Solution:
    def isValid(self, s: str) -> bool:
        closingMap={
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack=[]
        for char in s:
            #pop until opening bracket
            if char in closingMap:      
                if not(stack and stack.pop()==closingMap[char]):   #there is no corresponding opening bracket or stack is empty
                    return False
            else:
                stack.append(char)
        return False if stack else True
