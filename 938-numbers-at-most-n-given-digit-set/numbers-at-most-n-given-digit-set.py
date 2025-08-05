class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        main = str(n)
        N = len(main)
        m = len(digits)
        @cache
        def get(n):
            if n==0:
                return 1
            total = 0
            for i in range(m):
                total+= get(n-1)
            return total
        @cache
        def get_last(idx,isless):
            if idx==N:
                # print(s)
                return 1
            t = 0
            for x in digits:
                if not isless:
                    if int(x) < int(main[idx]):
                        t+= get_last(idx+1,True)
                    if int(x) == int(main[idx]):
                        t+= get_last(idx+1,isless)
                else:
                    t+= get_last(idx+1,isless)
            return t
        res = 0
        for i in range(1,N):
            res += get(i)
        # print(res)
        res += get_last(0,False)
        return res