class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                opr2=stack.pop()
                opr1=stack.pop()
                if token=="+":   res=opr1+opr2
                elif token=="-": res=opr1-opr2
                elif token=="*": res=opr1*opr2
                else           : res=int(opr1/opr2)
                stack.append(res)
            else:
                stack.append(int(token))
            # print(stack)
        return stack[-1]