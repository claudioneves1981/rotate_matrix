matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
    return matrix

print("Original Matrix:")
for row in matrix:
    print(row)

print("Rotated Matrix:")
for row in rotate_matrix(matrix):
    print(row)