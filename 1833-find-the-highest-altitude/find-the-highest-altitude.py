class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = 0
        maxi = 0
        for x in gain:
            s+=x
            maxi = max(maxi,s)
        return maxi