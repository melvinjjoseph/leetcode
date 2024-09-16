class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins=[]
        for time in timePoints:
            t=time.split(":")
            m=int(t[0])*60+int(t[1])
            mins.append(m)
        mins.sort()
        # print(mins)
        mini=mins[0]-mins[-1]+1440
        for i in range(1,len(mins)):
            mini=min(mini, mins[i]-mins[i-1])
        return mini