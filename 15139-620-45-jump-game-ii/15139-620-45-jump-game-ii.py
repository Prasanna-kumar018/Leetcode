class Solution:
    def jump(self, nums: List[int]) -> int:
        # GREEDY
        i = 0
        n = len(nums)
        if n==1:
            return 0
        count=0
        while i<n:
            maxi = nums[i]
            des = nums[i]+i
            next = -1
            while i<=min(des,n-1):
                if i+nums[i]>maxi:
                    maxi=i+nums[i]
                    next=i
                i+=1
            count+=1
            if des>=n-1:
                return count
            if next==-1:
                return -1
            i = next
        return count
