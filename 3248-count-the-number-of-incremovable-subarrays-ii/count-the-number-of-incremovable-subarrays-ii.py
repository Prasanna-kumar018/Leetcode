class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**20
        nums.append(INF)
        suffix = collections.deque()
        suffix.append((INF,n))
        """
        [prefix] + ... + [suffix]

        ... which is removed 
        """
        # suffix part
        for i in range(n-1,-1,-1):
            if nums[i]<nums[i+1]:
                suffix.appendleft((nums[i],i))
            else:
                break
        # no of suffix subarray
        total = min(n,len(suffix))
        print(suffix,total)
        for i in range(n):
            #prefix part
            if i>0 and nums[i-1]>=nums[i]:
                break
            while len(suffix)>1 and suffix[0][0]<=nums[i]:
                suffix.popleft()
            # print(i,suffix)
            val = 0
            if suffix and suffix[0][1]==i+1:
                val = 1
            total += len(suffix)-val
        return total