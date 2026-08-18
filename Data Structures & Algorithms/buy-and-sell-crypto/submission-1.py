class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_sell = None, None

        for price in prices:
            if not min_buy or price < min_buy:
                min_buy = price
                continue

            if not max_sell or price > max_sell:
                max_sell = price
                continue

        return max_sell - min_buy if min_buy and max_sell else 0
