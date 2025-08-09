class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        need = 1
        coins.append(target+1) # to make the need equal to target
        coins.sort()
        print(coins)
        n = len(coins)
        i = count = 0
        while i<n:
            if coins[i]<=need:
                need+=coins[i]
                i+=1
            else:
                need+= need
                count+=1
        return count