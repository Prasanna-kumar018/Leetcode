class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        """
        - (0,0,0) with effective value ((1 | 1) & 1) = 1
        - (0,0,1) with effective value ((1 | 1) & 4) = 0
        - (1,1,0) with effective value ((4 | 4) & 1) = 0
        - (1,1,1) with effective value ((4 | 4) & 4) = 4

        - (0,1,0) with effective value ((1 | 4) & 1) = 1
        - (1,0,0) with effective value ((4 | 1) & 1) = 1
        - (0,1,1) with effective value ((1 | 4) & 4) = 4
        - (1,0,1) with effective value ((4 | 1) & 4) = 4


        0 1 2 3

        0 0 0
        0 0 1
        0 0 2
        0 0 3
        1 1 0
        1 1 1
        1 1 2
        1 1 3
        2 2 0
        2 2 1
        2 2 2
        2 2 3
        3 3 0
        3 3 1
        3 3 2
        3 3 3 

        """
        n = len(nums)
        res = v = 0
        for i in range(n):
            # v ^= (nums[i]|nums[i])
            v ^= nums[i]
        for j in range(n):
            res ^= (v & nums[j])
        return res