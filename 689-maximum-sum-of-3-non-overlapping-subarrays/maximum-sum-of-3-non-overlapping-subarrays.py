class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]*n
        for i in range(1,n):
            prefix[i] = (prefix[i-1]+nums[i])
        def get(x,y):
            return prefix[y]- (prefix[x-1] if x-1>=0 else 0)
        INF = -10**10
        ans = []
        @cache
        def recur(idx,value):
            nonlocal ans
            if value==0:
                return (0,[])
            if idx==-1:
                return (INF,[])
            res, a = recur(idx-1,value)
            if idx-k>=-1:
                val , t = recur(idx-k,value-1)
                e = get(idx-k+1,idx)
                val += e
                s = []
                if len(t)<3:
                    s = list(t)
                    s.append(idx-k+1)
                if val > res:
                    a = s
                    res = val
                elif val==res and sorted(s) < sorted(a):
                    a = s
            return (res,a)
        x = recur(n-1,3)
        # print(x)
        return x[1]