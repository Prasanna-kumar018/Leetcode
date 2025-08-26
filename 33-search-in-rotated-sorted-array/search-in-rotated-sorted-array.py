class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r= 0,n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid+1
        ans = r
        l,r = 0,n-1
        while l<=r:
            mid = (l+r)//2
            real = (mid+ans)%n
            if nums[real]<target:
                l=mid+1
            elif nums[real]>target:
                r = mid-1
            else:
                return real
        return -1