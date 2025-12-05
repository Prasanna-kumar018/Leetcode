class Solution:
    def smallestValue(self, n: int) -> int:
        def get(x):
            i = 2
            s = 0
            v = x
            while i*i<=v:
                while x%i==0:
                # Because of this Loop all the Prime factors will only become as i
                    s += i
                    x //= i
                i+=1
            if x>1: # This will be Prime For sure ....
                s += x
            return s

        while n!=get(n):
            n = get(n)

        return n
