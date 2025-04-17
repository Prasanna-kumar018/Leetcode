class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        d  = collections.defaultdict(list)
        m = len(nums)
        for i in range(m):
            for j in range(len((nums[i]))):
                d[nums[i][j]].append(i)
        res = sorted([[x,y] for x,y in d.items()])
        # print(res)
        s = {}
        l,r = 0,-1
        n = len(res)
        diff = float('inf')
        a, b = -1,-1
        while r<n:
            if len(s)==m:
                if res[r][0]-res[l][0]<diff:
                    a,b = res[l][0],res[r][0]
                    diff = res[r][0]-res[l][0]
                for val in res[l][1]:
                    s[val]-=1
                    if s[val]==0:
                        del s[val]
                l+=1
            else:
                r+=1
                if r<n:
                    for val in res[r][1]:
                        s[val]=s.get(val,0)+1
        return [a,b]