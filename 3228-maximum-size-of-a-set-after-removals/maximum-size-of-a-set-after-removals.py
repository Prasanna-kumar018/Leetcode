class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        n =  len(nums1)
        inter = s1 & s2
        s1 = s1 - inter
        s2 = s2 - inter
        for x in inter:
            if len(s1)  < n//2:
                s1.add(x)
            else:
                s2.add(x)

        return min(n//2,len(s1)) + min(n//2,len(s2))