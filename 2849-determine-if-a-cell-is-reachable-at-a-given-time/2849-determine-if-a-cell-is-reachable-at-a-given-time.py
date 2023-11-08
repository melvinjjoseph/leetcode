class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy and t==1:
            return False
        minTime=max(abs(sx-fx), abs(sy-fy))
        if minTime>t:
            return False
        return True