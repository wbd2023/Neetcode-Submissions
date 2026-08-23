class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: i for i, char in enumerate(s)}
        prev = -1
        result = []

        for i, char in enumerate(s):
            if i > prev:
                result.append(1)
            else:
                result[-1] += 1

            prev = max(prev, last[char])

        return result
