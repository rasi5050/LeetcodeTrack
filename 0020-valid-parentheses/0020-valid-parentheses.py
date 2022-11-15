class Solution:
    def isValid(self, s: str) -> bool:
        mapping={')':'(', '}':'{', ']':'['}
        stack=[]
        for item in s:
            if item == '(' or item == '{' or item == '[':
                stack.append(item)
            elif item == ')' or item == '}' or item == ']':
                #pop until corresponding bracket
                while stack and stack[-1]!=mapping[item] and stack[-1] in [')',']','}']:
                    stack.pop()
                if stack and stack[-1]==mapping[item]:
                    stack.pop()
                else:
                    return False
        return False if stack else True
        