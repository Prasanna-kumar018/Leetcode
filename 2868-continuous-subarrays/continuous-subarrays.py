class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        l,r = 0,0
        # val,idx
        res = 0
        maxq = collections.deque()
        minq = collections.deque()
        while r<N:
            val = nums[r]
            while maxq and val > maxq[-1][0]:
                maxq.pop()
            maxq.append((val,r))
            while minq and val < minq[-1][0]:
                minq.pop()
            minq.append((val,r))
            while maxq and minq and maxq[0][0]-minq[0][0] > 2:
                if maxq[0][1]==l:
                    maxq.popleft()
                if minq[0][1]==l:
                    minq.popleft()
                l+=1
            res += (r-l+1)
            r+=1
        return  res