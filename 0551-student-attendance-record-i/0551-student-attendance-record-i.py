class Solution:
    def checkRecord(self, s: str) -> bool:
        prev1=prev2=''
        absent=0
        for i in s:
            if i=="A":
                absent+=1
            if absent>=2:
                return False
            if i=="L" and prev1=="L" and prev2=="L":
                return False
            elif i=="L" and prev1=="L":
                prev2="L"
            elif i=="L":
                prev1="L"
            else:
                prev1=prev2=''
        return True