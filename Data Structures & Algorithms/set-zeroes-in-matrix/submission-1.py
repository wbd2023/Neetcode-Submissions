class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # display(matrix)

        m, n = len(matrix), len(matrix[0])
        max_i, max_j = m - 1, n - 1

        erased_i, erased_j = set(), set()

        for i, line in enumerate(matrix):
            for j, cell in enumerate(line):
                if cell == 0:
                    erased_i.add(i)
                    erased_j.add(j)

        for i, line in enumerate(matrix):
            for j, cell in enumerate(line):
                if i in erased_i or j in erased_j:
                    matrix[i][j] = 0

        # display(matrix)


def display(matrix: List[List[int]]) -> None:
    for line in matrix:
        print(line)

    print()
