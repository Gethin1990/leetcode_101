# %% [markdown]
# 695. 岛屿的最大面积
# >https://leetcode-cn.com/problems/max-area-of-island/
# >给定一个二维的 0-1 矩阵，其中 0 表示海洋，1 表示陆地。单独的或相邻的陆地可以形成岛屿，每个格子只与其上下左右四个格子相邻。求最大的岛屿面积

# %%
def dfs(guid, _cur_i, _cur_j) -> int:
    if (
        _cur_i < 0
        or _cur_j < 0
        or _cur_i == len(guid)
        or _cur_j == len(guid[0])
        or guid[_cur_i][_cur_j] != 1
    ):
        return 0
    guid[_cur_i][_cur_j] = 0
    ans = 1
    for _di, _dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        _next_i = _cur_i + _di
        _next_j = _cur_j + _dj
        ans += dfs(guid, _next_i, _next_j)
    return ans


def max_area_of_island(guid) -> int:
    ans = 0
    for _i, _l in enumerate(guid):
        for _j, _ in enumerate(_l):
            ans = max(dfs(guid, _i, _j), ans)
    return ans


# %%
def max_area_of_island_test():
    guid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    result = max_area_of_island(guid)
    print(result)


max_area_of_island_test()


# %% [markdown]
# 547. 省份数量
# >https://leetcode-cn.com/problems/number-of-provinces/
# >有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
# >省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
# >给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
# >返回矩阵中 省份 的数量。


# %%


def find_circle_num(is_connected) -> int:
    def dfs(_i):
        for _j in range(provinces):
            if is_connected[_i][_j] == 1 and _j not in _visited:
                _visited.add(_j)
                dfs(_i)

    provinces = len(is_connected)
    _visited = set()
    circle = 0
    for _i in range(provinces):
        if _i not in _visited:
            dfs(_i)
            circle += 1
    return circle


# %%
def find_circle_num_test():
    is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result = find_circle_num(is_connected)
    print(result)


find_circle_num_test()
