class Solution:
    def maximum69Number (self, num: int) -> int:
        numstr=str(num)
        newstr=""
        f=0
        for s in numstr:
            if s=='6' and f==0:
                newstr+='9'
                f=1
            else:
                newstr+=s
        return int(newstr)