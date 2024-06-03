class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        for j in s:
            if i<len(t) and j==t[i]:
                i+=1
        return len(t[i:])
        