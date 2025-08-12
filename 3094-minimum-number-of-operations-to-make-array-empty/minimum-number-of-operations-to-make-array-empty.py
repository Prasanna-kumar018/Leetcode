class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        """
        We generate any num from 2 to INF
        using 2,3
        eg 4
        divide by 3 -> 3: 1 , 2: 0
        3:0 , 2: 2 -->
        """
        ans = 0
        for x,t in c.items():
            if t==1:
                return -1
            ans += (t//3)
            if t % 3 > 0:
                ans += 1
        return ans