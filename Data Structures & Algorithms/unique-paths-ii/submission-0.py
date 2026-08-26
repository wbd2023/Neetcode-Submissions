class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (1, 0)]  # Right + Down.

        m, n = len(obstacleGrid[0]), len(obstacleGrid)

        display(obstacleGrid)

        for r, line in enumerate(obstacleGrid):
            for c, cell in enumerate(line):
                if r == c == 0:
                    obstacleGrid[r][c] = 1
                    continue

                if cell == 1:
                    obstacleGrid[r][c] -= 1
                    continue

                for dr, dc in DIRECTIONS:
                    if not (0 <= r - dr < m and 0 <= c - dc < n):
                        continue

                    obstacleGrid[r][c] += obstacleGrid[r - dr][c - dc]

        display(obstacleGrid)

        return obstacleGrid[m - 1][n - 1]


def display(grid: List[List[int]]) -> None:
    for line in grid:
        print(line)

    print()
