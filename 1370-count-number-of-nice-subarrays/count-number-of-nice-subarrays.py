class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def atmost(k):
            l,r=0,0
            have = 0
            res = 0
            while r<n:
                if nums[r]%2==1:
                    have+=1
                while have>k and l<=r:
                    if nums[l]%2==1:
                        have-=1
                    l+=1
                res+=(r-l+1)
                r+=1
            return res
        return atmost(k)-atmost(k-1)