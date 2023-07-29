class Solution:
    def checkValidString(self, s: str) -> bool:
        lmin,lmax=0,0
        for i in range(len(s)):
            if s[i]=='(':
                lmin+=1
                lmax+=1
            elif s[i]==')':
                lmin=max(0,lmin-1)
                lmax-=1
            else:
                lmin=max(0,lmin-1)
                lmax+=1
            if lmax<0:
                return False
            
        return lmin==0
            
        