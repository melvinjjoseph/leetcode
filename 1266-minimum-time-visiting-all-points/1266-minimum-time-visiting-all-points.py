class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        curX=points[0][0]
        curY=points[0][1]
        d=0
        for i in range(1,len(points)):
            d+=max(abs(curX-points[i][0]),abs(curY-points[i][1]))
            curX=points[i][0]
            curY=points[i][1]
        return d