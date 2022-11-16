class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for elem in tokens:
            if elem in {'+','-','*','/'}:
                b,a=stack.pop(),stack.pop()
                if elem == '+':
                    stack.append(a+b)
                elif elem == '-':
                    stack.append(a-b)
                elif elem == '*':
                    stack.append(a*b)
                elif elem == '/':
                    stack.append(int(a/b))
            else:
                stack.append(int(elem))
        return stack.pop()
     