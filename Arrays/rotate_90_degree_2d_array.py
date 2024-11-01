def rotate_90_clockwise(matrix):
    return [row for row in zip(*matrix[::-1])]

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_90_clockwise(matrix)
for row in rotated_matrix:
    print(row)
