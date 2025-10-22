class Solution:
    def maximizeWin(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = [0]*(n+1)
        l = ans  = 0
        for r in range(n):
            while nums[r]-nums[l]>k:
                l+=1
            curr = r-l+1
            ans = max(ans,curr+best[l])
            best[r+1]=max(best[r],curr)
        return ans