class Solution:
    def findIndices(self, nums: List[int], index: int, value: int) -> List[int]:
        N = len(nums)
        INF = 10**20
        nums = [(val,ind) for ind,val in enumerate(nums)]
        nums.sort()
        l = 0 
        mini = INF
        # print(nums)
        maxi = -INF
        for r in range(N):
            while l<=r and abs(nums[l][0]-nums[r][0])>=value:
                mini = min(mini,nums[l][1])
                maxi = max(maxi,nums[l][1])
                l+=1
            # print(l,r,mini,maxi)
            if mini != INF and abs(nums[r][1]-mini)>=index:
                return [mini,nums[r][1]]
            if maxi !=  -INF and abs(nums[r][1]-maxi)>=index:
                return [maxi,nums[r][1]]
        return [-1,-1]