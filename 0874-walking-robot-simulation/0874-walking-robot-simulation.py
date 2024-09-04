class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle=set()
        for a,b in obstacles:
            obstacle.add((a,b))
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        res=0
        x,y=0,0
        cur_dir=0
        
        for com in commands:
            if com==-2:
                cur_dir=(cur_dir+3)%4
                continue
            if com==-1:
                cur_dir=(cur_dir+1)%4
                continue
            dx,dy=directions[cur_dir]
            for _ in range(com):
                if (x+dx,y+dy) in obstacle:
                    break
                x,y=x+dx,y+dy
            res=max(res,x**2+y**2)
        return res