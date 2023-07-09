class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        op=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]:
                temp,ind=stack.pop()
                op[ind]=i-ind
            stack.append([temperatures[i],i])
        return op         


            