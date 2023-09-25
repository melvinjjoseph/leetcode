class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=''.join(sorted(s))
        t=''.join(sorted(t))
        mlen=max(len(s),len(t))
        for i in range(mlen-1):
            if s[i]!=t[i]:
                return t[i] if len(t)>len(s) else s[i]
        if len(s)>len(t):
            return s[mlen-1]
        else:
            return t[mlen-1]
                