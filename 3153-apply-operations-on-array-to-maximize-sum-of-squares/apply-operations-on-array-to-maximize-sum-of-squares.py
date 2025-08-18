class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        """
        a + b = (a & b) + (a | b)
        i j  ni nj
        0 0  0  0
        0 1  0  1
        1 0  0  1  # what it means is we can pull the 1 
        1 1  1  1


        10110101
        10101010
        01010111

        so it becomes
        11111111
        10110111
        00000000

        move all the ones of the corresponding bit to the top
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