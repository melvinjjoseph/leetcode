class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        res=""
        prev2=s[0]
        prev=s[1]
        res=s[:2]
        for c in s[2:]:
            if c!=prev2 or c!=prev:
                res+=c
                prev2=prev
                prev=c
        return res