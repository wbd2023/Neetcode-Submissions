NO_COIN = False
YES_COIN = True


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        today = {NO_COIN: 0}

        for price in prices:
            tomorrow = {}

            for coinful, subtotal in today.items():
                tomorrow[NO_COIN] = subtotal

                match coinful:
                    case _ if coinful == NO_COIN:
                        tomorrow[YES_COIN] = (
                            min(tomorrow[YES_COIN], subtotal - price)
                            if YES_COIN in tomorrow
                            else subtotal - price
                        )

                    case _ if coinful == YES_COIN:
                        best = max(best, subtotal + price)

            today = tomorrow

        return best
