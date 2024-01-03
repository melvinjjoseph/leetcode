class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        tot=0
        prev=-1
        cur=0
        for s in bank[0]:
            if s=='1':
                cur+=1
        for row in bank[1:]:
            c=0
            for s in row:
                if s=='1':
                    c+=1
            if c==0:
                continue
            prev=cur
            cur=c
            tot+=prev*cur
        return tot
            