class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # display(matrix)

        min_i, max_i = 0, len(matrix) - 1
        min_j, max_j = 0, len(matrix[0]) - 1

        for i, line in enumerate(matrix):
            for j, cell in enumerate(line):
                if cell != 0:
                    continue

                matrix[min_i][j] = 0
                matrix[i][min_j] = 0

        # display(matrix)

        for i, line in enumerate(matrix):
            for j, cell in enumerate(line):
                if matrix[min_i][j] == 0 or matrix[i][min_j] == 0:
                    matrix[i][j] = 0

        # display(matrix)


def display(matrix: List[List[int]]) -> None:
    for line in matrix:
        print(line)

    print()
