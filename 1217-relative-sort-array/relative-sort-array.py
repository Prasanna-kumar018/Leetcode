class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for idx,val in enumerate(arr2):
            d[val]=idx
        def func(x):
            if x in d:
                return (0,d[x])
            return (1,x)
        arr1.sort(key=func)
        return arr1