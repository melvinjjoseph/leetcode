class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        op=''
        while(columnNumber):
            tmp=(columnNumber-1)%26
            op=chr(tmp+65)+op
            columnNumber=(columnNumber-1)//26
        return op