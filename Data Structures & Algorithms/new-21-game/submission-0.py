class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        before = Counter({0: 1})

        # At most `k` turns, if Alice only draws 1s.
        for _ in range(k):
            after = Counter()

            for current, chance in before.items():
                # Stop drawing once Alice has at least `k` points.
                if current >= k:
                    after[current] += chance
                    continue

                for additional in range(1, maxPts + 1):
                    total = min(n + 1, current + additional)
                    after[total] += chance / maxPts

            # print(f"before={before}")
            before = after
            # print(f"after={after}")

        # print(before.total(), before.get(n + 1, 0))

        return (before.total() - before.get(n + 1, 0)) / before.total()
