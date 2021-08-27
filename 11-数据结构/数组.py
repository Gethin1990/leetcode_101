# %% [markdown]
# 448. 找到所有数组中消失的数字
# >给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

#%%
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n = len(nums)
    dic = {}
    for _i in range(1, n + 1):
        dic[_i] = 0
    for _, val in enumerate(nums):
        dic[val] += 1

    return [k for k, v in dic.items() if v == 0]


#%%
def find_disappeared_numbers_test():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    res = find_disappeared_numbers(nums)
    print(res)


find_disappeared_numbers_test()


# %% [markdown]
# 48. 旋转图像
# >给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

# steps：
# 1. 假设边长4x4的矩阵，_n 作为索引计算变量为4-1
# 2. 画出矩阵，以0，1为起点进行推算
# 3. 把矩阵分割为4块，_row = 4/2;逐圈搜索框架：_column>=row & <n-row
#%%
def rotate(matrix: list[list[int]]) -> list[list[int]]:
    _n = len(matrix) - 1
    # 4x4 _row=0,column =1, n =3
    for _row in range(_n // 2 + 1):  # 闭区间+1
        for _column in range(_row, _n - _row):
            (
                matrix[_column][_n - _row],  # (1,3)
                matrix[_n - _row][_n - _column],  # (3,2)
                matrix[_n - _column][_row],  # (2,0)
                matrix[_row][_column],  # (0,1)
            ) = (
                matrix[_row][_column],  # (0,1)
                matrix[_column][_n - _row],  # (1,3)
                matrix[_n - _row][_n - _column],  # (3,2)
                matrix[_n - _column][_row],  # (2,0)
            )

    return matrix


#%%
def rotate_test():
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    res = rotate(matrix)
    print(res)


rotate_test()

# %% [markdown]
# 240. 搜索二维矩阵 II
# >给定一个二维矩阵，已知每行和每列都是增序的，尝试设计一个快速搜索一个数字是否在矩阵中存在的算法。

# %%
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    rows = len(matrix)
    columns = len(matrix[0])
    for _row in range(0, rows):
        for _column in range(columns - 1, -1, -1):
            if target == matrix[_row][_column]:
                return True
    return False


# %%
def search_matrix_test():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 18
    res = search_matrix(matrix, target)
    print(res)


search_matrix_test()

# %% [markdown]
# 769. 最多能完成排序的块
# >数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。我们最多能将数组分成多少块？

#%%
def max_chunks_to_sorted(arr: list[int]) -> int:
    ans = m = 0
    for _i, val in enumerate(arr):
        m = max(m, val)
        if m == _i:
            ans += 1
    return ans


#%%
def max_chunks_to_sorted_test():
    arr = [1, 0, 2, 3, 4]
    res = max_chunks_to_sorted(arr)
    print(res)


max_chunks_to_sorted_test()
# %%
