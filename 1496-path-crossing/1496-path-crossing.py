class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited=set() 
        visited.add((0,0))
        x=0
        y=0
        for s in path:
            if s=='N':
                y+=1
            if s=='S':
                y-=1
            if s=='E':
                x+=1
            if s=="W":
                x-=1
            if (x,y) not in visited:
                visited.add((x,y))
            else:
                return True
        print(visited)
        return False