class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j=0
        for i in range(len(str1)):
            if str1[i]==str2[j]:
                j+=1
            elif str1[i]=='z' and str2[j]=='a':
                j+=1
            elif ord(str1[i])+1==ord(str2[j]):
                j+=1
            if j==len(str2):
                return True
        return False
        