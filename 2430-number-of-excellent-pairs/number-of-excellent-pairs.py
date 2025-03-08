class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = (set(nums))
        maxi = 32
        count = [0]*(maxi)
        for x in nums:
            count[x.bit_count()]+=1
        print(count)
        total = 0
        for i in range(maxi):
            for j in range(maxi):
                if i+j>=k:
                    total+=(count[i]*count[j])
        return total