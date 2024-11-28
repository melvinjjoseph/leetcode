class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS= len(grid), len(grid[0])
        
        dq=deque([(0,0,0)])
        
        visit=set([(0,0,0)])
        
        while dq:
            obs, r,c= dq.popleft()
            if r==ROWS-1 and c==COLS-1:
                return obs
            if r+1<ROWS and (r+1,c) not in visit:
                visit.add((r+1,c))
                if grid[r+1][c]:
                    dq.append((1+obs,r+1,c))
                else:
                    dq.appendleft((obs,r+1,c))
            if r-1>=0 and (r-1,c) not in visit:
                visit.add((r-1,c))
                if grid[r-1][c]:
                    dq.append((1+obs,r-1,c))
                else:
                    dq.appendleft((obs,r-1,c))
            if c+1<COLS and (r,c+1) not in visit:
                visit.add((r,c+1))
                if grid[r][c+1]:
                    dq.append((1+obs,r,c+1))
                else:
                    dq.appendleft((obs,r,c+1))
            if c-1>=0 and (r,c-1) not in visit:
                visit.add((r,c-1))
                if grid[r][c-1]:
                    dq.append((1+obs,r,c-1))
                else:
                    dq.appendleft((obs,r,c-1))
            
            
            