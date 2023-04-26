class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        else:
            op=0
            while(num>0):
                op=op+(num%10)
                num=num//10
            return self.addDigits(op)
