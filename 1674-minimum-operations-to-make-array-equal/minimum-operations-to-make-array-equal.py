class Solution:
    def minOperations(self, n: int) -> int:
        total = 0
        mid = (n-1)//2
        val = (2*mid)+1
        for idx in range(n):
            curr = 2*idx+1
            total += abs(curr-val)
        return total//2