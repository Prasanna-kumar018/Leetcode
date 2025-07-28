class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        nsee = [n]*n
        pse = [-1]*n
        stack = []
        mod = 10**9 + 7
        for i in range(n):
            x = arr[i]
            while stack and arr[stack[-1]]>=x:
                idx = stack.pop()
                nsee[idx]=i
            pse[i]=stack[-1] if stack else -1
            stack.append(i)
        res = 0
        for idx in range(n):
            right = nsee[idx]-idx
            left = idx-pse[idx]
            val = (right)*(left)*(arr[idx])
            res+= val
        return res%mod