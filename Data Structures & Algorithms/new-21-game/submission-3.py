class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Alice either never draws or cannot finish above `n`.
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        # Probability of reaching each score.
        chance = [0.0] * (n + 1)
        chance[0] = 1.0

        # Sum of drawable scores that can reach the current score.
        window = chance[0]
        result = 0.0

        for score in range(1, n + 1):
            chance[score] = window / maxPts

            # Only scores below `k` can lead to another draw.
            if score < k:
                window += chance[score]
            else:
                result += chance[score]

            # Remove scores too far behind to reach the next score.
            old = score - maxPts
            if old >= 0:
                window -= chance[old]

        return result
