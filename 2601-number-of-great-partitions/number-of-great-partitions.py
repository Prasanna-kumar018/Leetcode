class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre =[0]
        MOD = 10**9+7
        for i in range(n):
            pre.append(pre[-1]+nums[i])
        @cache
        def recur(idx,left):
            right = pre[idx]-left
            if idx==n:
                if left==k and right>=k:
                    return 1
                return 0
            if left==k and right>=k:
                return pow(2,n-idx,MOD)
            total = 0
            # left
            if left+nums[idx]>=k:
                total += recur(idx+1,min(k,right))
            else:
                total += recur(idx+1,left+nums[idx])
            # right     
            # if right+nums[idx]>=k:
            #     total+= recur(idx+1,left)
            # else:
            #     total += recur(idx+1,left)
            total+= recur(idx+1,min(k,left))
            return total%MOD
    
        return recur(0,0)

