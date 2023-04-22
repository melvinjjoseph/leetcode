class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split(" ")
        i=1
        while(len(l[-1*i])==0):
            i+=1
        return len(l[-i])
        