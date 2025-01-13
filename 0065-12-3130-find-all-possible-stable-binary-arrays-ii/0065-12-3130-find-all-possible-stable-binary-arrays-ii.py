class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 +7
        # @cache
        # def recur(ones,zeros,last):
        #     if ones ==0 and zeros==0:
        #         return 1
        #     total =0
        #     if last!=1:
        #         for i in range(1,min(ones+1,limit+1)):
        #             total += recur(ones-i,zeros,1)
        #     if last!=0:
        #         for i in range(1,min(zeros+1,limit+1)):
        #             total += recur(ones,zeros-i,0)
        #     return total%mod
        # return recur(one,zero,-1)



        # dp = collections.defaultdict(lambda :collections.defaultdict(lambda :collections.Counter()))
        dp = [[ {-1:0,0:0,1:0} for _ in range(zero+1) ]for _ in range(one+1)]

        # Always use table because TLE may occur
        for last in range(-1,2):
            dp[0][0][last]=1
        # print(dp)
        z = [ [ dp[0][i][1] ] for i in range(zero+1)]
        o = [ [ dp[i][0][0] ] for i in range(one+1)]

        # def get(a,x,y):
        #     return a[y]-(a[x-1] if x-1>=-len(a) else 0) # if u pass the array as an argument TLE may occur

        for ones in range(0,one+1):
            for zeros in range(0,zero+1):
                if ones==0 and zeros==0:
                    continue
                za,oa = -1,-1
                for last in range(-1,2):
                    total =0
                    if last!=1:
                        if ones>0:
                            x,y = -min(ones,limit),-1
                            total += z[zeros][y]-(z[zeros][x-1] if x-1>=-len(z[zeros]) else 0)
                        # for i in range(1,min(ones+1,limit+1)):
                        #     total += dp[ones-i][zeros][1]
                    if last!=0:
                        if zeros>0:
                            x,y = -min(zeros,limit),-1
                            total += o[ones][y]-(o[ones][x-1] if x-1>=-len(o[ones]) else 0)
                        # for i in range(1,min(zeros+1,limit+1)):
                        #     total += dp[ones][zeros-i][0]
                    total%=mod
                    dp[ones][zeros][last]=total
                    if last==1:
                        za = z[zeros][-1]+total
                    if last==0:
                        oa = o[ones][-1]+total
                z[zeros].append(za)
                o[ones].append(oa)
                    
        # print(dp)
        return dp[one][zero][-1]
