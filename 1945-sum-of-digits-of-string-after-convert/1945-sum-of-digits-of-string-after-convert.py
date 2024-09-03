class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t=""
        for i in s:
            t+=str(ord(i)-96)
        for i in range(k):
            p=0
            for j in t:
                p+=int(j)
            t=str(p)
        return int(t)
            