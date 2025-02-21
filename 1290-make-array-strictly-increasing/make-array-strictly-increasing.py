class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        m = len(arr1)
        n = len(arr2)
        s = sorted(arr2)
        INF = 10**10
        @cache
        def recur(idx,prev,isArray2): # 2k * 2  * 2
            nonlocal s
            if idx==m:
                return 0
            best = INF
            prevvalue = s[prev] if isArray2 else arr1[prev]
            if prevvalue < arr1[idx]:
                best = min(best,recur(idx+1,idx,False))
            index = bisect.bisect_right(s,prevvalue)
            if 0<= index < len(s) and s[index]>prevvalue:
                best = min(best,recur(idx+1, index,True)+1)
            return best
        key =  bisect.bisect_right(s,-1)
        x = min(recur(1,0,False),recur(1,key,True)+1)
        return x if x!=INF else -1