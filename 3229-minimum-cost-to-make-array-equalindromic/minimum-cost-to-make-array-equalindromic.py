class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        N = len(nums)
        """
        123456

        122221 (nearest palindrome before x)
        123321  x
        124421 (nearest palindrome after x)


        12345

        12221 (nearest palindrome before x)
        12321 x
        12421 (nearest palindrome after x)

        Edge case

        median -> 1000
        then   -> 9 10 11
        digit length is reduced in case of 9 
        thats why we are running the loop of all length for digit 9 at last
        """
        # find median
        nums.sort()
        INF = 10**20
        def get(x):
            print (x)
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
        for L in range(1,10):
            res = min(res,go(int(str('9')*L)))
        return res