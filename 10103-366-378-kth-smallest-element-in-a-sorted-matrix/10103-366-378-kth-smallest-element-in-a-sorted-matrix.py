class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#       Time Complexity :- O(n*logn)
        m = len(matrix)
        n = len(matrix[0])
        def isSafe(val):
            count = 0
            row ,col = 0,n-1
            while row<m and col>=0:
                if matrix[row][col]>val:
                    col-=1
                else:
                    count+=col+1
                    row+=1
            return count>=k
        mini = matrix[0][0]
        maxi = matrix[-1][-1]
        l,r = mini,maxi
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                ans = mid
                r =mid-1
            else:
                l = mid+1
        return ans