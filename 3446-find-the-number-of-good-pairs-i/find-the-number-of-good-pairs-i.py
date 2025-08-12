class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        from collections import Counter
        m = len(nums1)
        n = len(nums2)
        # for finding the factors the time complexity would be square root of n
        # or j*j <= i
        M = max(nums1)
        lookup = collections.Counter()
        xx = Counter(nums1)
        for x,count in xx.items():
            i = 1
            while i*i<=x:
                if i*i==x:
                    lookup[i]+=count
                elif x%i==0:
                    lookup[i]+=count
                    lookup[x//i]+=count
                i+=1
        ans = 0
        for i in nums2:
            val =i*k
            ans += lookup[val]
        return ans