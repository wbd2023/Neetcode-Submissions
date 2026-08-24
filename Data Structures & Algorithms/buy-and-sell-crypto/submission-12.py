class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, best = None, 0

        for price in prices:
            # print(price, lowest, best)
            # print()

            if lowest is None:
                lowest = price
                continue

            lowest = min(lowest, price)
            best = max(best, price - lowest)

        return best
