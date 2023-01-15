class Solution:
    def isValid(self, s: str) -> bool:
        map={
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack=[]
        for char in s:
            #pop until opening bracket
            if char in map:
                if stack and stack[-1]==map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return False if stack else True