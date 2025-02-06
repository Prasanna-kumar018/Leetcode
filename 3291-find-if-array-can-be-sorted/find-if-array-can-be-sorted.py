class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = [(val,idx) for idx,val in enumerate(nums)]
        arr.sort()
        # print(arr)
        i = 0
        while i<n:
            t = i
            bits = bin(nums[i]).count('1')
            mini = maxi = arr[i][1]
            while t+1<n and bin(nums[t+1]).count('1')==bits:
                maxi =  max(maxi,arr[t+1][1])
                mini = min(mini,arr[t+1][1])
                t+=1
            # print(i,t)
            if mini!=i or maxi!=t:
                return False
            i=t+1
        return True