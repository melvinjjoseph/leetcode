class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap={}
        c=0
        for i in s:
            if i not in hashmap:
                hashmap[i]=1
            else:
                c+=2
                hashmap.pop(i)
        if len(hashmap)!=0:
            c+=1
        return c