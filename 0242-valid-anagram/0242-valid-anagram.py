class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        smap=defaultdict(int)
        tmap=defaultdict(int)
        for e in s:
            smap[e]+=1
        for e in t:
            tmap[e]+=1
        for letter in smap:
            if smap[letter]!=tmap[letter]:
                return False
        return True