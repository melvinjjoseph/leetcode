class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        op=''
        while(i<len(word1) and i<len(word2)):
            op=op+word1[i]
            op=op+word2[i]
            i+=1
        if(i<len(word1)):
            op=op+word1[i:len(word1)]
        if(i<len(word2)):
            op=op+word2[i:len(word2)]
        return op
            
        