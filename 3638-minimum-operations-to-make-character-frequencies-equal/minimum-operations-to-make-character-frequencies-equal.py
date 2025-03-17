class Solution:
    def makeStringGood(self, s: str) -> int:
        s= [ord(x)-ord('a') for x in s]
        INF = 10**20
        f = collections.Counter(s) # if element is not in Counter it returns 0
        maxi = max(f.values())

        """
        instead of doing two shift we can do insert or delete so that is reduntant
        Note that you cannot change 'z' to 'a' using the third operation.
        """
        print(f)
        def g(target):
            @cache
            def go(index,left):
                if index == 26:
                    return 0
                curr = f[index]
                best = INF
                if curr==target:
                    best = min(best,go(index+1,0))

                # delete
                if curr > target:
                    best = min(best,go(index+1,0)+(curr-target))
                else:
                    best = min(best,go(index+1,0)+curr)
                # upgrade
                if curr>target:
                    best = min(best,go(index+1,(curr-target))+(curr-target))
                else:
                    best = min(best,go(index+1,curr)+curr)

                # insert
                if curr<target:
                    x = (target-curr)-left
                    best = min(best,go(index+1,0)+max(0,x))
                    # using previous delete count for current insertion
                    # which is replacement or Change one character
                return best

            r = go(0,0)
            print(target,r)
            go.cache_clear()
            return r
        
        best = INF
        for x in range(maxi+1):
            best = min(best,g(x))
        return best
        