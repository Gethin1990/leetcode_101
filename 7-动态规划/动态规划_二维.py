# %% [markdown]
# 64. 最小路径和
# >https://leetcode-cn.com/problems/minimum-path-sum/
# >给定一个m  n 大小的非负整数矩阵，求从左上角开始到右下角结束的、经过的数字的和最小的路径。每次只能向右或者向下移动。

# steps:
# 1. def dp[][]
# 2. dp init
# 3. process rows & columns
# 4. dp 推导式

# %%
def min_path_sum(grid: list[list[int]]):
    rows = len(grid)
    columns = len(grid[0])
    dp = [[0] * columns for _ in range(rows)]
    dp[0][0] = grid[0][0]
    for _i in range(1, rows):
        dp[_i][0] = dp[_i - 1][0] + grid[_i][0]
    for _j in range(1, columns):
        dp[0][_j] = dp[0][_j - 1] + grid[0][_j]
    for _i in range(1, rows):
        for _j in range(1, columns):
            dp[_i][_j] = min(dp[_i - 1][_j], dp[_i][_j - 1]) + grid[_i][_j]
    return dp[rows - 1][columns - 1]


# %%
def min_path_sum_test():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = min_path_sum(grid)
    print(res)


min_path_sum_test()


# %% [markdown]
# 542. 01 矩阵
# >https://leetcode-cn.com/problems/01-matrix/
# >给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。


# steps:
# def dp with max value and h x w
# init dp
# if not 0,正斜线找临近的i-1和j-1点,获取临近的最小值
# if not 0,负斜线找临近的i+1和j+1点,获取临近的最小值


#%%
def update_matrix(matrix: list[list[int]]):
    if not matrix:
        return
    rows, columns = len(matrix), len(matrix[0])
    dp = [[float("INF")] * columns for _ in range(rows)]
    for _i in range(rows):
        for _j in range(columns):
            if matrix[_i][_j] == 0:
                dp[_i][_j] = 0
            else:
                if _j > 0:
                    dp[_i][_j] = min(dp[_i][_j], dp[_i][_j - 1] + 1)
                if _i > 0:
                    dp[_i][_j] = min(dp[_i][_j], dp[_i - 1][_j] + 1)

    for _i in range(rows - 1, -1, -1):
        for _j in range(columns - 1, -1, -1):
            if _j < columns - 1:
                dp[_i][_j] = min(dp[_i][_j], dp[_i][_j + 1] + 1)
            if _i < rows - 1:
                dp[_i][_j] = min(dp[_i][_j], dp[_i + 1][_j] + 1)

    return dp


#%%
def update_matrix_test():
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    res = update_matrix(mat)
    print(res)


update_matrix_test()


# %% [markdown]
# 221. 最大正方形
# >https://leetcode-cn.com/problems/maximal-square/
# >给定一个二维的 0-1 矩阵，求全由 1 构成的最大正方形面积。


# steps
# 1. def (row x columns) dp with 0
# 2. init dp
# 3. 正方形推导式： f[i][j] = min(f[i-1][j],f[i][j-1],f[i-1][j-1])+1
# 4. val =1 为有效 取最大边长

# %%
def maximal_square(matrix: list[list[str]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    max_side = 0
    rows, columns = len(matrix), len(matrix[0])
    dp = [[0] * columns for _ in range(rows)]
    for _i in range(rows):
        for _j in range(columns):
            if matrix[_i][_j] == "1":
                if _i == 0 or _j == 0:
                    dp[_i][_j] = 1
                else:
                    dp[_i][_j] = (
                        min(dp[_i - 1][_j], dp[_i][_j - 1], dp[_i - 1][_j - 1]) + 1
                    )
                max_side = max(max_side, dp[_i][_j])

    return max_side * max_side


#%%
def maximal_square_test():
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    res = maximal_square(matrix)
    print(res)


maximal_square_test()

# %%
