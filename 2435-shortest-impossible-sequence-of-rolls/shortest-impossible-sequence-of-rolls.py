class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        found = [set()]
        for x in rolls:
            found[-1].add(x)
            if len(found[-1])==k:
                found.append(set())
        return len(found)