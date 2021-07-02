# %%
from typing import List

# %% [markdown]
#  69. Sqrt(x) (Easy)
#  >给定一个非负整数，求它的开方，向下取整。

# %%


def my_sqrt(x: int) -> int:
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l+r)//2
        if mid*mid <= x:
            ans = mid
            l = mid+1
        else:
            r = mid-1
    return ans

# %%


def my_sqrt_test():
    result = my_sqrt(8)
    print(result)


# %%


def search_range(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    l = 0
    r = n
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            start = mid-1
            end = mid+1
            while start >= 0 and nums[start] == target:
                start -= 1
            while end < n and nums[end] == target:
                end += 1
            return[start+1, end-1]
        elif nums[mid] < target:
            l = mid+1
        else:
            r = mid
    return [-1, -1]

# %%


def search_range_test():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    result = search_range(nums, target)
    print(result)


# %%
# my_sqrt_test()
search_range_test()
