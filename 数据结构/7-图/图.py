# %% [markdown]
# 785. 判断二分图
# https://leetcode-cn.com/problems/is-graph-bipartite/

#%%
def is_bipartite(graph: list[list[int]]) -> bool:
    n = len(graph)
    UNCOLORED, RED, GREEN = 0, 1, 2
    color = [UNCOLORED] * n
    valid = True

    def dfs(node: int, c: int):
        nonlocal valid
        color[node] = c
        cNei = GREEN if c == RED else RED
        for neighbor in graph[node]:
            if color[neighbor] == UNCOLORED:
                dfs(neighbor, cNei)
                if not valid:
                    return
            elif color[neighbor] != cNei:
                valid = False
                return

    for i in range(n):
        if color[i] == UNCOLORED:
            dfs(i, RED)
            if not valid:
                break

    return valid


#%%
def is_bipartite_test():
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    result = is_bipartite(graph)
    print(result)


is_bipartite_test()


# %% [markdown]
# 210. 课程表 II
# https://leetcode-cn.com/problems/course-schedule-ii/

#%%


def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    res = []
    visited = [0] * numCourses
    adjacent = [[] for _ in range(numCourses)]

    def dfs(i):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        visited[i] = 1
        for j in adjacent[i]:
            if not dfs(j):
                return False

        visited[i] = 2
        res.append(i)
        return True

    for cur, pre in prerequisites:
        adjacent[cur].append(pre)
    for i in range(numCourses):
        if not dfs(i):
            return []
    return res


#%%
def find_order_test():
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = find_order(4, prerequisites)
    print(result)


find_order_test()
# %%
