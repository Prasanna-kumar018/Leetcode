class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        """
        a + b = (a & b) + (a | b)
        """
        MOD = 10**9 + 7
        n = len(nums)
        M = 32
        bits = [0]*M
        for x in nums:
            for i in range(M):
                if (x & (1<<i))>0:
                    bits[i]+=1
        arr = [] # arr can contains element such as zero
        for i in range(n):
            c = 0
            for j in range(M):
                if bits[j]>0:
                    bits[j]-=1
                    c |= (1<<j)
            arr.append(c)
        ans = 0
        for i in range(k):
            val = arr[i]
            ans += val**2
            ans %= MOD
        return ans 