class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        res = 0
        ncr = [[0]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(min(k+1,i+1)):
                if j==0:
                    ncr[i][j]=1
                else:
                    ncr[i][j]=(ncr[i][j-1]*(i-j+1)//j)
                    #ncr[i][j]=ncr[i][j-1]*((i-j+1)//j) this is wrong floor division
        for i in range(n):
            for j in range(k):
                res+= (nums[i]*(ncr[n-1-i][j]+ncr[i][j]))
                res%=mod
        return res