# %% [markdown]
# 934. 最短的桥
# >https://leetcode-cn.com/problems/shortest-bridge/
# >给定一个二维0-1 矩阵，其中1 表示陆地，0 表示海洋，每个位置与上下左右相连。已知矩阵中有且只有两个岛屿，求最少要填海造陆多少个位置才可以将两个岛屿相连。


# step:
# 1. for i,j to find the isload begin(val==1)
# 2. use dfs to find the isload
#   2.1 dfs framework
#   2.2 dfs return condition
#   2.3 find the isload start point
#   2.4 add the local to temp q
# 3. use bfs to find the short way
#   3.1 bfs framework based on temp q
#   3.2 bfs continue condition
#   3.3 try find next island
#   3.4 put the not found point to temp q for next search

# %%
def shortest_bridge(nums: list[list[int]]):
    import queue

    dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
    temp_q = queue.Queue()
    H = len(nums)
    W = len(nums[0])

    def dfs(_i, _j):
        if (
            _i < 0
            or _i >= H
            or _j < 0
            or _j >= W
            or nums[_i][_j] == 0
            or nums[_i][_j] == 2
        ):
            return

        if nums[_i][_j] == 1:
            nums[_i][_j] = 2
            temp_q.put((_i, _j))

            for _x, _y in dirs:
                _new_i, _new_j = _i + _x, _j + _y
                dfs(_new_i, _new_j)

    def bfs():
        steps = 0
        while temp_q:
            for _ in range(temp_q.qsize()):
                _i, _j = temp_q.get()
                for _x, _y in dirs:
                    _new_i, _new_j = _i + _x, _j + _y
                    if (
                        _new_i < 0
                        or _new_i >= H
                        or _new_j < 0
                        or _new_j >= W
                        or nums[_new_i][_new_j] == 2
                    ):
                        continue
                    if nums[_new_i][_new_j] == 1:
                        return steps
                    nums[_new_i][_new_j] = 2
                    temp_q.put((_new_i, _new_j))
            steps += 1

    for _i, row in enumerate(nums):
        for _j, val in enumerate(row):
            if val == 1:
                dfs(_i, _j)
                stp = bfs()
                return stp


#%%
def shortest_bridge_test():
    A = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
    ]
    res = shortest_bridge(A)
    print(res)


shortest_bridge_test()

# %%
