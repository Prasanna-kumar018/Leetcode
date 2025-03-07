class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True]*max(2,(right+1))
        prime[0]=False
        prime[1]=False
        for x in range(2,right+1):
            if prime[x]:
                for j in range(2*x,right+1,x):
                    prime[j]=False
        diff = 10**20 
        res = [-1,-1]
        prev = -1  
        for x in range(left,right+1):
            if prime[x]:
                if prev!=-1:
                    if x-prev < diff:
                        diff = x-prev
                        res = [prev,x]
                prev = x
        return  res