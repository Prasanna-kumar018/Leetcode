class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        """
        (p, q, r, s)
        nums[p] * nums[r] == nums[q] * nums[s]

        nums[p] / nums[q] == nums[s]/ nums[r]
        """
        events = collections.defaultdict(list)
        count = collections.Counter()
        for s in range(n-1,-1,-1):
            for r in range(s-2,-1,-1):
                g = gcd(nums[s],nums[r])
                key = (nums[s]//g , nums[r]//g)
                events[r].append(key)
                count[key]+=1
        ans = 0
        for q in range(n):

            # remove
            for d in [0,1]:
                for x in events[q+d]:
                    count[x]-=1
                events[q+d] = []
            
            for p in range(q-1):
                g = gcd(nums[q],nums[p])
                key = (nums[p]//g,nums[q]//g)
                ans += count[key]
        return ans