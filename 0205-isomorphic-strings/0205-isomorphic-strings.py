class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap={}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]]=t[i]
            else:
                if hashmap[s[i]]!=t[i]:
                    return False
        hashmap={}
        for i in range(len(s)):
            if t[i] not in hashmap:
                hashmap[t[i]]=s[i]
            else:
                if hashmap[t[i]]!=s[i]:
                    return False
        return True
                
        