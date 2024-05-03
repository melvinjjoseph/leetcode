class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        if len(v1)>len(v2):
            f=1
        elif len(v2)>len(v1):
            f=2
        else:
            f=0
        i=0
        while i<len(v1) and i<len(v2):
            if int(v1[i])> int(v2[i]):
                return 1
            if int(v1[i])< int(v2[i]):
                return -1
            i+=1
        if f==0:
            return 0
        
        while i<len(v1) or i<len(v2):
            if f==1 and int(v1[i])>0:
                return 1
            if f==2 and int(v2[i])>0:
                return -1
            i+=1
        return 0