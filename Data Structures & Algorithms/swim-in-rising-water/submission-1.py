Position = tuple[int, int]


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        start: Position = (0, 0)
        highest = grid[0][0]

        frontier: list[tuple[int, Position]] = [(highest, start)]
        visited: set[Position] = {start}

        while frontier:
            height, (r, c) = heapq.heappop(frontier)
            highest = max(highest, height)

            if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
                return highest

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    continue

                if (nr, nc) in visited:
                    continue

                heapq.heappush(frontier, (grid[nr][nc], (nr, nc)))
                visited.add((nr, nc))

        raise AssertionError("unreachable")
