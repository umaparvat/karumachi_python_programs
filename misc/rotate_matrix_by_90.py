def rotate(matrix):
    #code here
    m = len(matrix)
    n = len(matrix[0])
    for row in range(m):
        i = 0
        j = n-1
        while i < j:
            matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]
            i += 1
            j -= 1
    print(matrix)
    for row in range(0, m):
        for col in range(row+1, n):
            print((row, col), "swao", (col, row))
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    return matrix

if __name__ == "__main__":
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(rotate(matrix))