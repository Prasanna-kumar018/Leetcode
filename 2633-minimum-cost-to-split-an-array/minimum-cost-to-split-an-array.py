class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = 10**20
        @cache
        def recur(idx):
            if idx>=n:
                return 0
            count = Counter()
            res = 0
            ans = INF
            for i in range(idx,n):
                count[nums[i]]+=1

                if count[nums[i]]==2:
                    res+=2
                elif count[nums[i]]>=3:
                    res+=1
                ans = min(ans,recur(i+1)+k+res)
            return ans
        return recur(0)