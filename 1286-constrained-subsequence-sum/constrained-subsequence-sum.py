class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        maxq = collections.deque() # val,idx

        for idx,val in enumerate(nums):
            nums[idx] += maxq[0][0] if maxq else 0
            while maxq and nums[idx]>maxq[-1][0]:
                maxq.pop()
            
            if nums[idx]>0:
                maxq.append((nums[idx],idx))
                """
                the maxq elements should be positive because it is going to be added to the array
                elements.If it contains negative it will lower the value of array elements
                """
            if maxq and maxq[0][1]==idx-k:
                maxq.popleft()
        return max(nums)