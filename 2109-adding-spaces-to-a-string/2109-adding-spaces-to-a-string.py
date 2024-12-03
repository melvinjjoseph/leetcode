class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces=set(spaces)
        res=[]
        for i in range(len(s)):
            if i in spaces:
                res.append(" ")
            res.append(s[i])
        return "".join(res)