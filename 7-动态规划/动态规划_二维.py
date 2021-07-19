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


def update_matrix(matrix: list[list[int]]):
    if not matrix:
        return
    h, w = len(matrix), len(matrix[0])
    dp = [float("inf") * w for _ in range(h)]
    for _i in range(h):
        for _j in range(w):
            if matrix[_i][_j] == 0:
                dp[_i][_j] = 0
            else:
                if _j>0:
                    dp
