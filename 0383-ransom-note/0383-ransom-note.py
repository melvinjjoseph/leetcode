class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        hashmap={}
        for s in magazine:
            if s not in hashmap:
                hashmap[s]=1
            else:
                hashmap[s]+=1
        for s in ransomNote:
            if s not in hashmap:
                return False
            if hashmap[s]>0:
                hashmap[s]-=1
            else:
                return False
        return True
            