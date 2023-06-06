class TimeMap:

    def __init__(self):
        self.dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key]=[]
        self.dict[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        if timestamp < self.dict[key][0][1]:
            return ""
        l=0
        r=len(self.dict[key])
        mid=0
        while(l<r):
            mid=(l+r)//2
            if self.dict[key][mid][1]<=timestamp:
                l=mid+1
            else:
                r=mid
        return "" if r==0 else self.dict[key][r-1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)