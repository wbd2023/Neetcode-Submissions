class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (1, 0)]  # Right + Down.

        n, m = len(obstacleGrid), len(obstacleGrid[0])

        display(obstacleGrid)

        for r, line in enumerate(obstacleGrid):
            for c, cell in enumerate(line):
                if cell == 1:
                    obstacleGrid[r][c] = 0
                    continue

                if r == c == 0:
                    obstacleGrid[r][c] = 1
                    continue

                for dr, dc in DIRECTIONS:
                    if not (0 <= r - dr < n and 0 <= c - dc < m):
                        continue

                    obstacleGrid[r][c] += obstacleGrid[r - dr][c - dc]

        display(obstacleGrid)

        return obstacleGrid[n - 1][m - 1]


def display(grid: List[List[int]]) -> None:
    for line in grid:
        print(line)

    print()
