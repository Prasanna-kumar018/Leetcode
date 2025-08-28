class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxq = collections.deque() # val,idx
        maxq.append((nums[0],0))
        for r in range(1,n):
            nums[r]+=maxq[0][0] if maxq else 0
            while maxq and nums[r]>maxq[-1][0]:
                maxq.pop()
            maxq.append((nums[r],r))
            left = r-k
            if maxq and maxq[0][1]==left:
                maxq.popleft()
        return nums[-1]