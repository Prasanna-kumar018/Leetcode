class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = []
        """
        bisect.bisect_left()
        1 1 2 2 
        1 second one replaces the first one (>= greater than or equal to )


        bisect.bisect_right()
        1 1 2 2 
        1 1 second one won't replaces the first one (> greater than )
        """
        for x in nums:
            ind = bisect.bisect_right(l,x)
            if ind==len(l):
                l.append(x)
            else:
                l[ind]=x
        return len(nums)-len(l)