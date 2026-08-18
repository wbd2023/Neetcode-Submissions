class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        today = set()

        for price in prices:
            tomorrow = {-price}

            for coinful, subtotal in today:
                tomorrow.add()

            today = tomorrow

        return best
