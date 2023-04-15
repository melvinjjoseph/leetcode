class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        StringSet=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in StringSet:
                StringSet.remove(s[l])
                l+=1
            StringSet.add(s[r])
            res=max(res,r-l+1)
        return res        