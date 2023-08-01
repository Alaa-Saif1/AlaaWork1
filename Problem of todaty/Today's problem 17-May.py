def rotate(matrix, left_rotation_time):
    n = len(matrix)
    left_rotation_time = left_rotation_time % n
    rotated_ma = matrix.copy()

    for i in range(left_rotation_time):
        element1 = rotated_ma[0]
        for i in range(n - 1):
            rotated_ma[i] = rotated_ma[i + 1]
        rotated_ma[n - 1] = element1

    return rotated_ma

array = [1, 2, 3, 4, 5]
left_rotation_time = 2

res = rotate(array, left_rotation_time)
print(res)