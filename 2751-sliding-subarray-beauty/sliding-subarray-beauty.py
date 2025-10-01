class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, xx: int) -> List[int]:
        n = len(nums)
        MAXI = abs(min(nums)) 
        count = [0]*(MAXI+1)
        ans  = []
        for i in range(k):
            if nums[i]<0:
                count[abs(nums[i])]+=1
        for r in range(k,n+1):
            c = 0
            val = 0
            for x in range(MAXI,-1,-1):
                if count[x]>0:
                    prev = c
                    c += count[x]
                    if prev < xx and  c>=xx:
                        val = x
            ans.append(-val)
            l = r-k
            if nums[l]<0:
                count[abs(nums[l])]-=1
            if r<n and nums[r]<0:
                count[abs(nums[r])]+=1
        return ans