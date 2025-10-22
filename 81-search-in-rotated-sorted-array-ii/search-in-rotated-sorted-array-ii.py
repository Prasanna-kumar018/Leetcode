class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        f = False
        for x in nums:
            if x==target:
                f = True
        return f