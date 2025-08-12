class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        total = 0
        have = 0
        d = collections.defaultdict(int)
        for i in range(k-1):
            if nums[i] not in d:
                have+=1
            d[nums[i]]+=1
            total += nums[i] 
        l,r = 0,k-1
        ans = 0
        while r<n:
            total += nums[r]
            if nums[r] not in d:
                have+=1
            d[nums[r]]+=1
            # print(have,total)
            if have>=m:
                ans = max(total,ans)
            d[nums[l]]-=1
            if d[nums[l]]==0:
                del d[nums[l]]
                have-=1
            total -= nums[l]
            l+=1
            r+=1
        return ans
