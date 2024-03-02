class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1=-1
        count_0=0
        for ele in s:
            if ele=='0':
                count_0+=1
            else:
                count_1+=1
        op=""
        while count_1:
            op+="1"
            count_1-=1
        while count_0:
            op+="0"
            count_0-=1
        op+="1"
        return op