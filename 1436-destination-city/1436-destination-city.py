class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start=set()
        end=set()
        for path in paths:
            start.add(path[0])
            end.add(path[1])
        dest=end.difference(start)
        return list(dest)[0]