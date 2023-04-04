class Solution:
    def partitionString(self, s: str) -> int:
        lastSeen=[-1]*26
        count=1
        start=0
        
        for i in range(len(s)):
            if lastSeen[ord(s[i]) - ord('a')] >= start:
                count += 1
                start = i
            lastSeen[ord(s[i]) - ord('a')] = i

        return count
            
        