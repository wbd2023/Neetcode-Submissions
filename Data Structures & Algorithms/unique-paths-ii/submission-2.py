class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        display(obstacleGrid)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        for r, line in enumerate(obstacleGrid):
            for c, cell in enumerate(line):
                if cell == 1:
                    obstacleGrid[r][c] = 0
                    continue

                if r == c == 0:
                    obstacleGrid[r][c] = 1
                    continue

                obstacleGrid[r][c] += obstacleGrid[r - 1][c] if 0 <= r - 1 < m else 0
                obstacleGrid[r][c] += obstacleGrid[r][c - 1] if 0 <= c - 1 < n else 0

        display(obstacleGrid)

        return obstacleGrid[m - 1][n - 1]


def display(grid: List[List[int]]) -> None:
    for line in grid:
        print(line)

    print()
