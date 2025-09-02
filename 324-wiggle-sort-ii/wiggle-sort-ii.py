class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = sorted(nums)
        n = len(nums)
        i = (n-1)//2
        for j in range(0,n,2):
            nums[j]=num[i]
            i-=1
        i = n-1
        for j in range(1,n,2): 
            nums[j]=num[i]
            i-=1