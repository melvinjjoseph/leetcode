class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        prev = points[0]
        count = 1
        for i in range(1, len(points)):
            curr_start_point, curr_end_point = points[i]
            prev_start_point, prev_end_point = prev
            
            if curr_start_point > prev_end_point:
                count += 1
                prev = points[i]
            else:
                prev[0] = max(prev_start_point, curr_start_point)
                prev[1] = min(prev_end_point, curr_end_point)
                
        return count