class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return (numBottles*numExchange-1)//(numExchange-1)
s = Solution()
print(s.numWaterBottles(9,3))