class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        m = len(mana)
        n = len(skill)
        prev = [None]*n
        start = 0
        for j in range(n):
            start+=(skill[j]*mana[0])
            prev[j]=start
        print(prev)
        for i in range(1,m):
            start = prev[0]
            t = 0
            for j in range(1,n):
                t += (mana[i]*skill[j-1])
                start = max(start,prev[j]-t)
            for j in range(n):
                start+= ((mana[i]*skill[j]))
                prev[j]=start
            # print(prev)
        return prev[-1]