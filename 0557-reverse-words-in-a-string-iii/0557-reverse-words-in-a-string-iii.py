class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        s=''
        for i in range(len(l)):
            s+=l[i][::-1]
            if i!=len(l)-1:
                s+=' '
        return s