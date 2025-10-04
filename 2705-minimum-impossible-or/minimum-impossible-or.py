class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        """
        if we have these powers of 2 then inbetween numbers (-) can be created
        by bitwise or no need to check
        for example if we have 1 and 2 --> 3 can be generated
        for example if we have 1,2,3,4 -> 5,6,7 can be generated
        1 - 2 - 4 - 8 - 16
          01
          10
          11
         100
         101
         110
         111
        1000

        """
        need = 1
        s = set(nums)
        while need in s:
            need <<= 1 # need += need or need = 2*need
        return need