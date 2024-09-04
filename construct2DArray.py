def construct2DArray(original, m, n):
    two_dim_arr = [[0 for i in range(n)] for j in range(m)]

    if len(original) != m * n:
        return []

    index = 0
    for i in range(m):
        for j in range(n):
            two_dim_arr[i][j] = original[index]
            index += 1
    return two_dim_arr


print(construct2DArray(original = [1,2,3,4], m = 2, n = 2))
print(construct2DArray(original = [1,2], m = 1, n = 1))