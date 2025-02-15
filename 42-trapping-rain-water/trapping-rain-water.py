class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        res = 0
        ml,mr = 0,0
        while l<=r:
            if height[l]<=height[r]:
                res+=max(0,ml-height[l])
                ml = max(ml,height[l])
                l+=1
            else:
                res+=max(0,mr-height[r])
                mr = max(mr,height[r])
                r-=1
        return res
