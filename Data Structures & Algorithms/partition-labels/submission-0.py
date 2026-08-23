class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: i for i, char in enumerate(s)}
        prev = -1
        result = []

        for i, char in enumerate(s):
            # print(last)
            # print(prev)
            # print(result)
            # print(char)
            # print()

            if i > prev:
                result.append(1)
                prev = last[char]
                continue

            if i <= prev:
                result[-1] += 1
                prev = max(prev, last[char])
                continue

        return result
