class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ans = 0
        for i in range(n):
            res = None
            for j in range(i,n):
                if not res:
                    res = nums[j]
                else:
                    res = math.lcm(res,nums[j])

                if res==k:
                    ans += 1
            
        return ans