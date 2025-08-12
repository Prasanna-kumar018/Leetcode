class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        """
        nums[i]*nums[j] is divisible by k 

        so nums[i]*nums[j]  = K or 2k or 3k or 4k 
        so if the product contains K then its fine....
        """
        n = len(nums)
        M = max(nums)
        fact = [[] for _ in range(M+1) ]
        """
        the below code is also Sieve of Erosthenes (j+=x)

        Time O(M*logM)
        """
        for x in range(1,M+1):
            j = x
            while j<=M:
                fact[j].append(x)
                j+=x
        total = 0
        lookup = collections.Counter()
        for idx,val in enumerate(nums):
            now = gcd(val,k) # value would be atmost k

            total += lookup[k//now]
            for d in fact[val]:
                lookup[d]+=1

        return total
        

        