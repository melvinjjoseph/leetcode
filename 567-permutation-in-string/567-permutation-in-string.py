class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        def check():
            for i in range(len(s1count)):
                if s1count[i]!=s2count[i]:
                    return False
            return True
        s1count=[0]*26
        s2count=[0]*26
        
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')]+=1
            s2count[ord(s2[i])-ord('a')]+=1
        
        if check():
            return True
        l=0
        for r in range(len(s1),len(s2)):
            s2count[ord(s2[r])-ord('a')]+=1        
            s2count[ord(s2[l])-ord('a')]-=1
            l+=1
            if check():
                return True
        return False
            
            
            
            
            
        