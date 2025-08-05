class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        """
        (a+b) % p = (a%p) +(b%p)
        (a-b) % p = (a%p) -(b%p)
        (a-b) % p = (a%p) -(b%p)
        (a/b) % p = (a%p) *( inverse of b %p)
        (a/b) % p = (a%p) *( (b^-1) %p)

        fermat's little theorem
         
        x^ p % p ==> x % p if p is prime and p does not divide x
        divided by x^2
        x ^ (p-2) % p === x^(-1) %p

        therefore , a^(-1) % p = a^ (p-2) % p

        power = [1]*(n+1)
        for i in range(1,n+1):
            power[i] = (power[i-1]*2)%mod  
        this can be achieved by  pow(2,i,mod) but don't use this inbuilt inside the loop

        but this pow(base,exp,mod) is different from math.pow()
        """ 
        mod = 10**9 + 7
        n = len(nums)
        if n==1:
            return 0
        nums.sort()
        power = [1]*(n+1)
        for i in range(1,n+1):
            power[i] = (power[i-1]*2)%mod 
        ans = 0
        for i in range(n):
            ans += (nums[i]*power[i])
            ans -= (nums[i]*power[n-1-i])
        return ans%mod