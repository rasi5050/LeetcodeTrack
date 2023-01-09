class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            currWord=[]
            currNum=[]
            
            #keep popping
            if char ==']':
                while stack[-1]!='[':
                    currWord.append(stack.pop())
                stack.pop()         #poping opening bracket
                curWord="".join(currWord)
                currWord=currWord[::-1]
                while stack and stack[-1].isdigit():
                    currNum.append(stack.pop())
                currNum=int("".join(currNum)[::-1])
                stack+=list(currWord*currNum)
            else:    
                stack.append(char)
        return ''.join(stack)
        