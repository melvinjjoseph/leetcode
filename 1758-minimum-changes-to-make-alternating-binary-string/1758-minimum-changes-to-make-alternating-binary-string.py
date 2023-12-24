class Solution:
    def minOperations(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            if i%2==0 and s[i]=='0':
                c+=1
            if i%2==1 and s[i]=='1':
                c+=1
        mini=c
        c=0
        for i in range(len(s)):
            if i%2==1 and s[i]=='0':
                c+=1
            if i%2==0 and s[i]=='1':
                c+=1
                
        mini=min(c,mini)
        return mini