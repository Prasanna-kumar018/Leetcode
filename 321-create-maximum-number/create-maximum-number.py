class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m  = len(nums1)
        n  = len(nums2)
        def get(arr,need):
            drop = len(arr)-need
            s = []
            for x in arr:
                while s and s[-1]<x and drop>0:
                    drop-=1
                    s.pop()
                s.append(x)
            return s[:need] # definitely the length of the stack (s) would be greater than or equal to the need.
        ans  = []
        for i in range(k+1):
            l = i
            r = k-i
            if l<=m and r<=n:
                print(l,r)
                left = get(nums1,l)
                right = get(nums2,r)
                # here max calculate the lexicographically largest
                # [6,7,5] [6,3,5] we have to pop() 6 from arr1 
                # instead of arr2 since it is lexicographically largest....
                # max(left,right) returns the array... 
                res =[ max(left,right).pop(0)  for _ in (left+right)]
                
                # print(res)
                if res>ans:
                    ans = res
        return ans