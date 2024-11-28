class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS= len(grid), len(grid[0])
        
        pq=[(0,0,0)]
        
        visit=set([(0,0,0)])
        
        while pq:
            obs, r,c= heapq.heappop(pq)
            if r==ROWS-1 and c==COLS-1:
                return obs
            if r+1<ROWS and (r+1,c) not in visit:
                heapq.heappush(pq,(obs+grid[r+1][c],r+1,c))
                visit.add((r+1,c))
            if r-1>=0 and (r-1,c) not in visit:
                heapq.heappush(pq,(obs+grid[r-1][c],r-1,c))
                visit.add((r-1,c))
            if c+1<COLS and (r,c+1) not in visit:
                heapq.heappush(pq,(obs+grid[r][c+1],r,c+1))
                visit.add((r,c+1))
            if c-1>=0 and (r,c-1) not in visit:
                heapq.heappush(pq,(obs+grid[r][c-1],r,c-1))
                visit.add((r,c-1))
        
            
            
            