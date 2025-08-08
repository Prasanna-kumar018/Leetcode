class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        N = len(nums)
        # find median
        nums.sort()
        INF = 10**20
        def get(x):
            total = 0
            for y in nums:
                total += abs(x-y)
            return total

        def go(val):
            best = INF
            s = str(val)
            M = len(s)
            if M%2 ==0:
                x = s[:(M//2)] # s is a string so x is also a string
            else:
                x = s[:((M+1)//2)]
            val = int(x)

            for v in [val-1,val,val+1]: # Check for val-1 , val , val+1 to get the shortest palindrome 
                if M%2==0:
                    best = min(best,get(int(str(v) + ''.join(reversed(str(v))))))
                else:
                    best = min(best,get(int(str(v) + ''.join(reversed(str(v)[:-1])))))
            return best

        res = INF
        for median in [nums[N//2],nums[(N-1)//2]]:
            res = min(res,go(median))
        for i in range(1,10):
            for L in range(1,10):
                res = min(res,get(int(str(i)*L)))
        
        return res