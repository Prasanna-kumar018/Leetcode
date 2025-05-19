class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        d = {}
        for idx,val in enumerate(nums):
            d[idx]=val
        nums = [(x,idx) for idx,x in enumerate(nums)]
        nums.sort(key = lambda x: (sum(map(int,str(x[0]))),x[0],x[1]))
        count = 0
        i = 0
        n = len(nums)
        # print(nums)
        while i<n:
            while d[i]!=nums[i][0]:
                des = nums[i][1]
                nums[i],nums[des]=nums[des],nums[i]
                count+=1
            i+=1
        return count