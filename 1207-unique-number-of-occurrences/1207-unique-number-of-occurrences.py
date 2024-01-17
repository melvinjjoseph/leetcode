class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set1=set(arr)
        vals=[]
        for val in set1:
            vals.append(arr.count(val))
        return len(vals)==len(set(vals))