class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, best = None, 0

        for price in prices:
            if lowest is None:
                lowest = price
                continue

            best = max(best, price - lowest)
            lowest = min(lowest, price)

        return best
