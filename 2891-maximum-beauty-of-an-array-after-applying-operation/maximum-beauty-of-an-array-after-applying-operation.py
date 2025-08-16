class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        N = len(nums)
        MAXI = max(nums)
        arr = [0]*(MAXI+1)
        for idx,val in enumerate(nums):
            L = max(0,val-k)
            R = min(MAXI,val+k)
            arr[L]+=1
            if R+1<=MAXI:
                arr[R+1]-=1
        for i in range(1,MAXI+1):
            arr[i]+=arr[i-1]
        return max(arr)