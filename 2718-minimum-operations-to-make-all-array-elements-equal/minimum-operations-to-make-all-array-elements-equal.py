class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = []
        pre = [nums[0]]
        for i in range(1,n):
            pre.append(pre[-1]+nums[i])
        def get(x,y):
            if 0<= x < n and 0<= y <n and x<=y:
                return pre[y]-(pre[x-1] if x-1>=0 else 0)
            return 0
        for x in queries:
            idx = bisect.bisect_left(nums,x+1)-1
            L = idx+1
            R = n -1 - idx
            total = (L*x) - get(0,idx) - (R*x) + get(idx+1,n-1)
            ans.append(total)
        return ans