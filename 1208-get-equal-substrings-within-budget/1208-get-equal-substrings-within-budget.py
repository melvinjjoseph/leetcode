class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start=0
        maxlength=0
        cost=0
        for i in range(len(s)):
            cost+=abs(ord(s[i])-ord(t[i]))
            
            while cost>maxCost:
                cost-=abs(ord(s[start])-ord(t[start]))
                start+=1
            
            maxlength=max(maxlength,i-start+1)
        
        return maxlength