class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        q = []
        def push(val):
            heapq.heappush(q, val)
        def pop():
            return heapq.heappop(q)
        
        nums.sort()
        total = 0
        ans = -1
        # print(nums)
        for idx,x in enumerate(nums):
            if total>x and idx>=2:
                ans = max(ans,total+x)
            total += x
        return ans