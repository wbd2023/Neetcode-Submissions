from enum import Enum, auto


class Status(Enum):
    NO_COIN = auto()
    YES_COIN = auto()


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        today = {Status.NO_COIN: 0}

        for price in prices:
            tomorrow = today.copy()

            for coinful, subtotal in today.items():
                match coinful:
                    case Status.NO_COIN:
                        tomorrow[Status.YES_COIN] = (
                            max(tomorrow[Status.YES_COIN], 0 - price)
                            if Status.YES_COIN in tomorrow
                            else subtotal - price
                        )

                    case Status.YES_COIN:
                        tomorrow[Status.NO_COIN] = max(tomorrow[Status.NO_COIN], subtotal + price)

            today = tomorrow
            print(today)

        return today[Status.NO_COIN]
