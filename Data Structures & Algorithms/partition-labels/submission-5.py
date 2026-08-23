class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last, end = {char: i for i, char in enumerate(s)}, -1
        sizes = []

        for i, char in enumerate(s):
            if i > end:
                sizes.append(0)

            sizes[-1] += 1
            end = max(end, last[char])

        return sizes
