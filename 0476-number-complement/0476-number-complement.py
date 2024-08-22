class Solution:
    def findComplement(self, num: int) -> int:
        num_string=bin(num)[2:]
        op_num=""
        for i in num_string:
            if i=="0":
                op_num+="1"
            else:
                op_num+="0"
        return int(op_num,2)
    
        