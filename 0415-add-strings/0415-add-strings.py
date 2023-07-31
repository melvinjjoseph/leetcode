class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1,n2=[],[]
        op=[]
        if len(num1) < len(num2):
            num1 = '0' * (len(num2) - len(num1))+num1
        else:
            num2 = '0' * (len(num1) - len(num2))+num2
        for i in range(len(num1)):
            n1.append(int(num1[i]))
            n2.append(int(num2[i]))
        car=0
        while n1 and n2:
            pop1=n1.pop()
            pop2=n2.pop()
            suma=pop1+pop2+car
            op.append((suma)%10)
            car=suma//10
        if car:
            op.append(car)
        ops=""
        while op:
            ops+=str(op.pop())
        return ops