class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i]%=k
        # O(k*k*n)
        @cache
        def go(idx,rem):
            if idx==n:
                c = [0]*k
                c[rem]+=1
                return c
            ans = go(idx+1,(rem*nums[idx])%k)
            ans = ans[:] # this is  important O(k)
            ans[rem]+=1
            return ans
        res = [0]*k
        for i in range(n):
            f  = go(i+1,nums[i])
            for i in range(k):
                res[i]+=f[i]
        return res