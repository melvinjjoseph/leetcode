class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s=s+s+s
        if goal in s and len(goal)==len(s)//3:
            return True
        return False