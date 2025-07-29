class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0]*n
        right = [0]*n
        s = []
        for i in range(n):
            idx = bisect.bisect_left(s,nums[i])
            if idx==len(s):
                s.append(nums[i])
            else:
                s[idx]= nums[i]
            left[i]= idx+1
        s = []
        for i in range(n-1,-1,-1):
            idx = bisect.bisect_left(s,nums[i])
            if idx==len(s):
                s.append(nums[i])
            else:
                s[idx]= nums[i]
            right[i]= idx+1
        INF = 10**20
        res = INF
        # print(left,right)
        for idx in range(1,n-1):
            if left[idx]>1 and right[idx]>1:
                res = min(res,n-(left[idx]+right[idx]-1))
        return res