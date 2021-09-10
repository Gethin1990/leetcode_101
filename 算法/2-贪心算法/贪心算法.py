# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # 贪心算法

# %% [markdown]
# ##分配问题（find_content_children）

# %% [markdown]
# 455. Assign Cookies (Easy)
# >https://leetcode-cn.com/problems/assign-cookies/
# >有一群孩子和一堆饼干，每个孩子有一个饥饿度，每个饼干都有一个大小。每个孩子只能吃一个饼干，且只有饼干的大小不小于孩子的饥饿度时，这个孩子才能吃饱。求解最多有多少孩子可以吃饱。

# %%


def find_content_children(children: list[int], cookies: list[int]):
    children.sort()
    cookies.sort()
    _child, _cookie = [0, 0]
    while _child < len(children) and _cookie < len(cookies):
        if children[_child] <= cookies[_cookie]:
            _child += 1
            _cookie += 1
    return _child


def find_content_children_test():
    children = [1, 2]
    cookies = [1, 2, 3]
    result = find_content_children(children, cookies)
    print(result)


# %% [markdown]
# 135. Candy (Hard)
# >https://leetcode-cn.com/problems/candy/
# >一群孩子站成一排，每一个孩子有自己的评分。现在需要给这些孩子发糖果，规则是如果一个孩子的评分比自己身旁的一个孩子要高，那么这个孩子就必须得到比身旁孩子更多的糖果；所有孩子至少要有一个糖果。求解最少需要多少个糖果。

# %%


def candy(ratings: list[int]):
    l = len(ratings)
    num = [1 for _ in range(l)]
    for _i in range(l):
        if ratings[_i] > ratings[_i - 1] and _i - 1 >= 0:
            num[_i] = num[_i - 1] + 1
    for _i in range(l - 1, -1, -1):
        if ratings[_i] < ratings[_i - 1] and _i - 1 >= 0:
            num[_i - 1] = max(num[_i - 1], num[_i] + 1)
    return sum(num)


def candy_test():
    ratings = [1, 0, 2]
    result = candy(ratings)
    print(result)


# %% [markdown]
# 435. Non-overlapping Intervals (Medium)
# >https://leetcode-cn.com/problems/non-overlapping-intervals/ 
# >给定多个区间，计算让这些区间互不重叠所需要移除区间的最少个数。起止相连不算重叠。


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    delete = 0
    intervals.sort(key=lambda a: a[1])
    right = intervals[0][1]
    for _i in range(1, len(intervals)):
        if right > intervals[_i][0]:
            delete += 1
        else:
            right = intervals[_i][1]
    return delete


def erase_overlap_intervals_test():
    intervals = [[1, 2], [1, 3], [2, 4]]
    result = erase_overlap_intervals(intervals)
    print(result)


# %%
find_content_children_test()
candy_test()
erase_overlap_intervals_test()
