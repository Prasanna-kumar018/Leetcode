class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        f = collections.Counter(nums)
        curr = 1
        count = 0
        while target>0:
            if target % 2 == 1: # to check the LSB

                updated = True
                while updated:
                    updated = False
                    for x in sorted(f.keys()):
                        if x<curr and f[x]>=2:
                            val = f[x]//2
                            f[x] %= 2
                            f[x*2] += val
                            updated = True
                found = None
                for x in sorted(f.keys()):
                    if x>=curr and f[x]>0:
                        found = x
                        break
                while found != curr:
                    f[found]-=1
                    f[found//2]+=2
                    count+=1
                    found //= 2
                # found == curr
                f[found]-=1
            target //= 2 # target >>= 1 
            curr *= 2
        return count 