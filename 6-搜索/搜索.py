# %% [markdown]
#  695. 岛屿的最大面积
#  >给定一个二维的 0-1 矩阵，其中 0 表示海洋，1 表示陆地。单独的或相邻的陆地可以形成岛屿，每个格子只与其上下左右四个格子相邻。求最大的岛屿面积

# %%


class max_area_of_island_solution:
    def dfs(self, guid, cur_i, cur_j) -> int:
        if (
            cur_i < 0
            or cur_j < 0
            or cur_i == len(guid)
            or cur_j == len(guid[0])
            or guid[cur_i][cur_j] != 1
        ):
            return 0
        guid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i = cur_i + di
            next_j = cur_j + dj
            ans += self.dfs(guid, next_i, next_j)
        return ans

    def max_area_of_island(self, guid) -> int:
        ans = 0
        for i, l in enumerate(guid):
            for j, n in enumerate(l):
                ans = max(self.dfs(guid, i, j), ans)
        return ans

    def max_area_of_island_test(self):
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
        result = self.max_area_of_island(guid)
        print(result)


# %% [markdown]
#  547. 省份数量
#  >有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
#  >省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
#  >给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
#  >返回矩阵中 省份 的数量。


# %%
class find_circle_num_solution:
    def find_circle_num(self, is_connected) -> int:
        def dfs(i):
            for j in range(provinces):
                if is_connected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(i)

        provinces = len(is_connected)
        visited = set()
        circle = 0
        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circle += 1
        return circle

    def find_circle_num_test(self):
        is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        result = self.find_circle_num(is_connected)
        print(result)


# %%
# s1 = max_area_of_island_solution()
# s1.max_area_of_island_test()

s2 = find_circle_num_solution()
s2.find_circle_num_test()
# %%
