class DetectSquares:

    def __init__(self):
        self.countPts=defaultdict(int)
        self.pts=[]

    def add(self, point: List[int]) -> None:
        self.countPts[tuple(point)]+=1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res=0
        px,py=point
        for x,y in self.pts:
            if abs(x-px)!=abs(y-py) or x==px or y==py:
                continue
            res+=self.countPts[x,py]*self.countPts[px,y]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)