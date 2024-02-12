class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap=defaultdict(int)
        for i in s:
            hashmap[i]+=1
        for i in range(len(s)):
            if hashmap[s[i]]==1:
                return i
        return -1