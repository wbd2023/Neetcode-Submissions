class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        count, find = None, {word1, word2}

        for word in wordsDict:
            if count is not None:
                count += 1

            if word in find:
                if count is None:
                    count = 0
                    find.remove(word)
                    continue

                return count
