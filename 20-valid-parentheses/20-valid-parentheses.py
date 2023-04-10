class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open=['(','{','[']
        for c in s:
            if c in open:
                stack.append(c)
                continue
            if len(stack)==0:
                return False
            if c==']':
                popped=stack.pop()
                if popped!='[':
                    return False
            elif c=='}':
                popped=stack.pop()
                if popped!='{':
                    return False
            elif c==')':
                popped=stack.pop()
                if popped!='(':
                    return False
            else:
                return False
        if len(stack)==0:
            return True
            



        