NO_COIN = False
YES_COIN = True


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        today = [(NO_COIN, 0)]

        for price in prices:
            tomorrow = []

            for state in today:
                coinful, subtotal = state

                tomorrow.append(state)
                match coinful:
                    case _ if coinful == NO_COIN:
                        tomorrow.append((YES_COIN, subtotal - price))

                    case _ if coinful == YES_COIN:
                        best = max(best, subtotal + price)

            today = tomorrow

        return best
