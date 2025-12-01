class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        """
        [9,1,2,3,9], k = 3
        """
        pre = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            pre.append(pre[-1]+nums[i])
        def get(x,y):
            return pre[y]-(pre[x-1] if x-1>=0 else 0)
        INF = 10**20
        @cache
        def recur(prev,curr,left):
            if curr==n:
                if left==0 and prev==n-1:
                    return 0
                return -INF
            res = -INF
            # take
            res = max(res,(get(prev+1,curr)/(curr-prev)) + recur(curr,curr+1,left-1) )
            # not take
            res = max(res,recur(prev,curr+1,left))
            return res
        return recur(-1,0,k)