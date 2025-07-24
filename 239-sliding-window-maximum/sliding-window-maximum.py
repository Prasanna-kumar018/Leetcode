class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        maxq = collections.deque() # val,idx
        for i in range(k-1):
            val = nums[i]
            while maxq and val > maxq[-1][0]:
                maxq.pop()
            maxq.append((val,i))

        r = k-1
        ans = []
        while r<n:
            val = nums[r]
            while maxq and val > maxq[-1][0]:
                maxq.pop()
            maxq.append((val,r))
            ans.append(maxq[0][0])
            if maxq[0][1]==r-(k-1):
                maxq.popleft()
            r+=1
        return ans