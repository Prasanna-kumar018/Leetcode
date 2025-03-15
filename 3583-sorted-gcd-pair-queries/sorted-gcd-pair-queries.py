class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        maxi= max(nums)
        f = collections.Counter(nums)
        count = [0]*(maxi+1)
        for x in range(maxi,0,-1):
            c = 0
            i = x
            while i<=maxi:
                c+=f[i]
                i+=x
            # c denotes the no of number that x as a gcd...
            # c choose 2
            count[x] = (c*(c-1))//2
            y = x+x
            while y<=maxi:
                count[x]-=count[y]
                y+=x
        print(count)
        for i in range(1,maxi+1):
            count[i]=count[i-1]+count[i]
        ans = []
        for x in queries:
            ans.append(bisect.bisect_left(count,x+1))
        return ans