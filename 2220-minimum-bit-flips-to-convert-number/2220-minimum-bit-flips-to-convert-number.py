class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s1,s2=bin(start)[2:], bin(goal)[2:]
        s1,s2=s1[::-1], s2[::-1]
        c=0
        i=0
        while i<min(len(s1),len(s2)):
            if s1[i]!=s2[i]:
                c+=1
            i+=1
        if len(s1)>i:
            for i in range(i,len(s1)):
                if s1[i]=="1":
                    c+=1
        elif len(s2)>i:
            for i in range(i,len(s2)):
                if s2[i]=="1":
                    c+=1
        return c