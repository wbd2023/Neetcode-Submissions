class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # display(matrix)

        min_i, max_i = 0, len(matrix) - 1
        min_j, max_j = 0, len(matrix[0]) - 1

        for i, line in enumerate(matrix):
            for j, cell in enumerate(line):
                if cell != 0:
                    continue

                # Note: only previously visited cells can be updated.
                matrix[min_i][j] = 0
                matrix[i][min_j] = 0

        # display(matrix)

        for i in range(max_i, min_i - 1, -1):
            for j in range(max_j, min_j - 1, -1):
                if matrix[min_i][j] == 0 or matrix[i][min_j] == 0:
                    matrix[i][j] = 0

        # display(matrix)


def display(matrix: List[List[int]]) -> None:
    for line in matrix:
        print(line)

    print()
