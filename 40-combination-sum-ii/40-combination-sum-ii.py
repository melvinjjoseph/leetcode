class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(i,added,total):
            if total==target:
                res.append(added.copy())
                return
            if total>=target:
                return
            prev=-1
            for ind in range(i,len(candidates)):
                if prev==candidates[ind]:
                    continue
                added.append(candidates[ind])
                backtrack(ind+1,added,total+candidates[ind])
                n=added.pop()
                prev=candidates[ind]
        backtrack(0,[],0)
        return res
        