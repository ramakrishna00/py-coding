def is_possible(matrix, i, j, k):
    n = j
    while n > 0:
        if matrix[i][n-1] == k:
            return False
        n -= 1
    m = i
    while m > 0:
        if matrix[m-1][j] == k:
            return False
        m -= 1
    return True

def sudoku(matrix, i = 0, j = 0):
    if i >= len(matrix) or j >= len(matrix):
        return True
    if matrix[i][j] == 0:
        for k in range(1,len(matrix)+1):
            if is_possible(matrix, i, j, k):
                matrix[i][j] = k
                if sudoku(matrix, i, j + 1) and sudoku(matrix, i + 1, j):
                    return True
                matrix[i][j] = 0
        return False
    else:
        if is_possible(matrix, i, j, matrix[i][j]):
            return sudoku(matrix, i, j + 1) and sudoku(matrix, i + 1, j)
        return False
