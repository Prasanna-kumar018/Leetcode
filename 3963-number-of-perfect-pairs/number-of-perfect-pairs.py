class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        N = len(nums)
        count = 0
        """
        for a in range(-15,31):
            for b in range(-100,100):
                if min(abs(a - b), abs(a + b)) <= min(abs(a), abs(b)) and max(abs(a - b), abs(a + b)) >= max(abs(a), abs(b)):
                    print(a,b)

        
        if x>0 -2*x ---> -((x+1)//2)
               ((x+1)//2) ---> 2*x
        if x<0 -2*x ---> -((x+1)//2)
               ((x+1)//2) ---> 2*x

        so positive or negative does not matter
        """
        nums = sorted([abs(x) for x in nums])
        p = []
        for x in nums:
            right = bisect.bisect_right(p,2*x) # > 2*x
            left = bisect.bisect_left(p,(x+1)//2) # >= (x+1)//2
            count += right-left
            p.append(x)
        return count