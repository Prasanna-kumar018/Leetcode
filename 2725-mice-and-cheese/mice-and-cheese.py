class Solution:
    def miceAndCheese(self, a: List[int], b: List[int], k: int) -> int:
        arr = [(x,y) for x,y in zip(a,b)]
        arr.sort(key=lambda x:(x[1]-x[0]))
        n = len(arr)
        ans = 0
        for i,(x,y) in enumerate(arr):
            if i<k:
                ans += x
            else:
                ans += y
        return ans