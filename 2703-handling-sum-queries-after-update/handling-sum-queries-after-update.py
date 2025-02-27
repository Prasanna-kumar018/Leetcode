class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        # bit_count() is much faster which would take only logn time....
        s = sum(nums2)
        nums1.reverse()
        xor = int(''.join(map(str,nums1)),2)
        res = []
        for x,l,r in queries:
            if x==1:
                v = ((1<<(r-l+1))-1)
                xor ^= (v<<l)
            elif x==2:
                s += (xor.bit_count()*l)
            else:
                res.append(s)
        return res