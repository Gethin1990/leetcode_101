# %% [markdown]
# 46. 全排列
# >https://leetcode-cn.com/problems/permutations/
# >给定一个无重复数字的整数数组，求其所有的排列方式。


def permute(nums):
    def back_track(_first):
        if _first == n:
            res.append(nums[:])
            return
        for _i in range(_first, n):
            nums[_first], nums[_i] = nums[_i], nums[_first]  # 交换
            back_track(_first + 1)
            nums[_first], nums[_i] = nums[_i], nums[_first]  # 恢复nums

    n = len(nums)
    res = []
    back_track(0)
    return res


# %%
def permute_test():
    nums = [1, 2, 3]
    res = permute(nums)
    print(res)


permute_test()

# %% [markdown]
# 77. 组合
# >https://leetcode-cn.com/problems/combinations/
# >给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。


def combine(n: int, k: int) -> list[list[int]]:

    nums = [i for i in range(1, n + 1)]

    res = []

    def back_track(nums_cut, temp_res, _index):
        if len(temp_res) == k:
            res.append(temp_res[:])
            return

        for _i in range(_index, n):
            temp_res.append(nums[_i])
            back_track(nums_cut[_index:], temp_res, _i + 1)
            temp_res.pop()

    if n == 0 or k == 0:
        return res

    back_track(nums, [], 0)
    return res


#%%
def combine_test():
    n, k = 4, 2
    res = combine(n, k)
    print(res)


combine_test()

# %% [markdown]
# 79. 单词搜索
# >https://leetcode-cn.com/problems/word-search/
# >给定一个字母矩阵，所有的字母都与上下左右四个方向上的字母相连。给定一个字符串，求字符串能不能在字母矩阵中寻找到。


def exist(board: list[list[str]], word: str) -> bool:

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()

    def check(_i, _j, k):

        if board[_i][_j] != word[k]:  # 没找到对应的字母
            return False
        if k == len(word) - 1:  # 找到了所有的字母
            return True

        result = False
        visited.add((_i, _j))

        for _di, _dj in direction:
            _new_i, _new_j = _i + _di, _j + _dj
            if (
                0 <= _new_i < h and 0 <= _new_j < w and (_new_i, _new_j) not in visited
            ):  # 坐标条件约束
                if check(_new_i, _new_j, k + 1):  # 四个方向找字母
                    result = True
                    break

        visited.remove((_i, _j))

        return result

    h, w = len(board), len(board[0])
    for _i in range(h):
        for _j in range(w):
            if check(_i, _j, 0):
                return True

    return False


#%%
def exist_test():
    borad = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    res = exist(borad, word)
    print(res)


exist_test()
# %%
