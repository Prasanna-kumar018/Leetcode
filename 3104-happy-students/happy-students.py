class Solution:
    def countWays(self, nums: List[int]) -> int:
        N = len(nums)
        """
        [1,1]
        2 > min(1,1)-> students selected
           1          4
        [0,  2, 3, 3,    6, 6, 7, 7]
        0 
        """
        nums.sort()
        res = 0
        for i in range(N-1):
            if i+1>nums[i] and i+1<nums[i+1]:
                res += 1
        res += (0<nums[0])
        res += (nums[-1]<N)
        return res