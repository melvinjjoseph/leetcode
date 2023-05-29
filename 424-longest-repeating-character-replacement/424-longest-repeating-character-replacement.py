class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        l=0
        r=0
        hashset=[0]*26
        print(hashset)
        for r in range(len(s)):
            hashset[ord(s[r])-ord('A')]+=1
            while(r-l+1-max(hashset)>k):
                hashset[ord(s[l])-ord('A')]-=1
                l+=1
            longest=max(longest,r-l+1)
        return longest
            
            
            
        