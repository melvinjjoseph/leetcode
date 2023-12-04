class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxi=-1
        cur="m"
        for s in num:
            if s==cur[-1]:
                cur+=s
            else:
                cur=s
            if len(cur)==3:
                maxi=max(int(cur),maxi)
        if maxi==0:
            return "000"
        return str(maxi) if maxi!=-1 else ""