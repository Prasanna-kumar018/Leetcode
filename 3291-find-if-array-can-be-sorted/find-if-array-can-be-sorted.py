class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        pre = [bin(x).count('1') for x in nums]
        prefix = [0]*n
        prefix[0]=pre[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+pre[i]
        # print(prefix)
        res = [(val,idx) for idx,val in enumerate(nums)]
        res.sort()
        for i in range(n):
            src = res[i][1]
            des = i
            if pre[src]*abs(des-src+1) != abs(prefix[des]-(prefix[src-1] if src>0 else 0)):
                return False
        return True