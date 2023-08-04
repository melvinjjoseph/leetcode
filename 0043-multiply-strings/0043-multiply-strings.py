class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        res=[0]*(len(num1)+len(num2))
        num1, num2= num1[::-1], num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit=int(num1[i1])*int(num2[i2])
                res[i1+i2]+=digit
                res[i1+i2+1]+=res[i1+i2]//10
                res[i1+i2]=res[i1+i2]%10
                
                
        resstr=""
        print(res)
        f=0
        for i in range(len(res)-1,-1,-1):
            if f==0 and res[i]==0:
                continue
            else:
                f=1
                resstr+=str(res[i])
        return resstr