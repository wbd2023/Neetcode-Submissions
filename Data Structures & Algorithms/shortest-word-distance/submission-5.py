class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        PAIRS = {word1: word2, word2: word1}

        best = 3 * 10**4 + 1
        prevs: Dict[str, int | None] = {word1: None, word2: None}

        for i, word in enumerate(wordsDict):
            if word not in prevs:
                continue

            if prevs[PAIRS[word]] is not None:
                best = min(best, i - prevs[PAIRS[word]])

            prevs[word] = i

        return best
