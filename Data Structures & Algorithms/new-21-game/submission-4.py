class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Alice either never draws or cannot finish above `n`.
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        # Probability of reaching each score.
        probability = [0.0] * (n + 1)
        probability[0] = 1.0

        # Sum of probabilities at drawable scores that can reach the current score.
        drawable = probability[0]

        # Probability of stopping with at most `n` points.
        winning = 0.0

        for score in range(1, n + 1):
            # Each drawable score has one of `maxPts` draws that reaches `score`.
            probability[score] = drawable / maxPts

            # Continue drawing below `k`; otherwise Alice stops and wins.
            if score < k:
                drawable += probability[score]
            else:
                winning += probability[score]

            # Remove a score once it is too far behind to reach the next score.
            leaving = score - maxPts
            if leaving >= 0:
                drawable -= probability[leaving]

        return winning
