class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        pre = [arr[0]]
        n = len(arr)
        for i in range(1,n):
            pre.append(pre[-1]+arr[i])
        # print(pre)
        prefix = pre[:]
        for i in range(n):
            val = 0
            if i-2>=0:
                val = prefix[i-2]
            prefix[i]+=val
        # print(prefix)
        res = 0
        for r in range(n):
            count = (r+2)//2 
            val = (count*pre[r]-(prefix[r-1] if r-1>=0 else 0))
            res += val
            # print(res,val,count)
        return res