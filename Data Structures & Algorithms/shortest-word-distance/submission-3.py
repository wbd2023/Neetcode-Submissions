class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        best = 3 * 10**4 + 1

        for i, word in enumerate(wordsDict):
            if word != word1 and word != word2:
                continue

            target = word1 if word == word2 else word2
            for j, candidate in enumerate(wordsDict[i + 1:]):
                if candidate == target:
                    best = min(best, j + 1)
                    break

        return best
