class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)

        prefix = [nums[0]]
        for i in range(1,n):
            prefix.append(prefix[-1]+nums[i])

        def get(x,y):
            return prefix[y]-(prefix[x-1] if x-1>=0 else 0)
        # If we get one false then it is false for sure .....
        @cache
        def recur(left,right):
            if left==right:
                return True
            res = False
            for i in range(left,right):
                x = recur(left,i)
                L = i-left+1
                R = right-i
                y = recur(i+1,right)
                if (L==1 or get(left,i)>=m) and (R==1 or get(i+1,right)>=m) and x and y:
                    res = True
            return res
        x = recur(0,n-1)
        return x