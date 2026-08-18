from enum import Enum, auto


class Status(Enum):
    NO_COIN = auto()
    YES_COIN = auto()
    SOLD_COIN = auto()


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        today = {Status.NO_COIN: 0, Status.SOLD_COIN: 0}

        for price in prices:
            tomorrow = today.copy()

            for coinful, subtotal in today.items():
                match coinful:
                    case Status.NO_COIN:
                        tomorrow[Status.YES_COIN] = (
                            max(tomorrow[Status.YES_COIN], subtotal - price)
                            if Status.YES_COIN in tomorrow
                            else subtotal - price
                        )

                    case Status.YES_COIN:
                        tomorrow[Status.SOLD_COIN] = max(tomorrow[Status.SOLD_COIN], subtotal + price)

            today = tomorrow
            print(today)

        return today[Status.SOLD_COIN]
