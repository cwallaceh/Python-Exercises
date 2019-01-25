# Rotate Image

# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Follow up:
# Could you do this in-place?


def rotate_image(matrix):
    # We need to trade rows and convert them in columns
    rotated = [[] for i in range(len(matrix))]
    for row in range(len(matrix) - 1, -1, -1):
        for i, col in enumerate(matrix[row]):
            rotated[i].append(col)
    return rotated


def inplace_rotate_image(matrix):
    """TODO"""
    pass


matrix = [[0, 0, 1],
          [0, 1, 1],
          [1, 1, 1]]

print(rotate_image(matrix))