class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        ones = set()
        twos = set()
        three = set()
        for x in nums:
            ones.add(x)

            for y in ones:
                twos.add(y^x)
            
            for y in twos:
                three.add(y^x)
        return len(three)