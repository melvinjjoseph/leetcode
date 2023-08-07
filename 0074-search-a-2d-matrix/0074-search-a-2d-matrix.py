class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        val=0
        while(l<=r):
            mid=(l+r)//2
            if target>matrix[mid][-1]:
                l=mid+1
            elif target<matrix[mid][0]:
                r=mid-1
            else:
                val=mid
                break
        l=0
        r=len(matrix[val])-1
        while(l<=r):
            mid=(l+r)//2
            if matrix[val][mid]==target:
                return True
            elif matrix[val][mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False