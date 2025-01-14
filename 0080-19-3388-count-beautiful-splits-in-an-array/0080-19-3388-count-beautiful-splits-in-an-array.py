class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        d = 50
        """
        5 4 3 2 1 0 
        3 2 1 0
        """
        if n<=2:
            return 0
        mod = 10**7+7      # less modulus value can improve the time complexity
        power = [1]*(n+1)
        for i in range(1,n+1):
            power[i]= (power[i-1]*d)%mod
        hashPrefix = [0]*n
        hash = 0
        for i in range(n):
            hash = (hash*d)+nums[i]
            hash%=mod
            hashPrefix[i]=hash
        total = 0
        def isValid(s1,e1,s2,e2):
            len1 = e1-s1+1
            len2 = e2-s2+1
            if len1>len2:
                return False
            hash1 = (hashPrefix[e1]-((hashPrefix[s1-1] if s1-1>=0 else 0)*power[len1]))%mod
            hash2 = (hashPrefix[s2+len1-1]-((hashPrefix[s2-1] if s2-1>=0 else 0)*power[len1]))%mod
            return hash1==hash2 
        for i in range(1,n):   # 0 - before i , i to before j , j to n-1
            for j in range(i+1,n):
                len1 = i
                len2 = j-i
                len3 = n-j
                # x = isValid(0,i-1,i,j-1)                 
                # y = isValid(i,j-1,j,n-1)  the number of calls may be reduced

                
                # print(i,j,x,y)    
                if  (len2>=len1 and isValid(0,i-1,i,j-1)) or (len3>=len2 and isValid(i,j-1,j,n-1)):
                    total+=1
        return total             