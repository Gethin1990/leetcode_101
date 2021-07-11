# %% [markdown]
#  695. 岛屿的最大面积
#  >给定一个二维的 0-1 矩阵，其中 0 表示海洋，1 表示陆地。单独的或相邻的陆地可以形成岛屿，每个格子只与其上下左右四个格子相邻。求最大的岛屿面积

# %%

class max_area_of_island_solution:
    def dfs(self,guid, cur_i, cur_j) -> int:
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


    def max_area_of_island(self,guid) -> int:
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


# %%
s1 = max_area_of_island_solution()
s1.max_area_of_island_test()

# %%
