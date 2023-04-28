class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops=['+','-','*','/']
        for s in tokens:
            if s in ops:
                op1=stack.pop()
                op2=stack.pop()
                if s=='+':
                    stack.append(op1+op2)
                elif s=='-':
                    stack.append(op2-op1)
                elif s=='*':
                    stack.append(op1*op2)
                else:
                    stack.append(int(op2/op1))
            else:
                stack.append(int(s))
        return stack[0]