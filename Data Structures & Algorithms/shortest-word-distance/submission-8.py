class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pair = {word1: word2, word2: word1}
        last: Dict[str, int | None] = {word1: None, word2: None}

        best = len(wordsDict)

        for i, word in enumerate(wordsDict):
            if word not in last:
                continue

            prev = last[pair[word]]
            if prev is not None:
                best = min(best, i - prev)

            last[word] = i

        return best
