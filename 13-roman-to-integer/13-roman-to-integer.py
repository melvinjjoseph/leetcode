class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        for i in range(0,len(s)-1):
            if roman[s[i]]>=roman[s[i+1]]:
                num=num+roman[s[i]]
            else:
                num=num-roman[s[i]]
        num=num+roman[s[len(s)-1]]
        return num