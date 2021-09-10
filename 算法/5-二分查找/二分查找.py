# %% [markdown]
# 69. Sqrt(x) (Easy)
# >https://leetcode-cn.com/problems/sqrtx/
# >给定一个非负整数，求它的开方，向下取整。


def my_sqrt(x: int) -> int:
    _l, _r, tmp = 0, x, -1
    while _l <= _r:
        _mid = (_l + _r) // 2
        if _mid * _mid <= x:
            tmp = _mid
            _l = _mid + 1
        else:
            _r = _mid - 1
    return tmp


def my_sqrt_test():
    result = my_sqrt(8)
    print(result)


my_sqrt_test()

# %% [markdown]
# 34. Find First and Last Position of Element in Sorted Array (Medium)
# >https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/ 
# >给定一个增序的整数数组和一个值，查找该值第一次和最后一次出现的位置。


def search_range(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    _l = 0
    _r = n - 1
    while _l < _r:
        _mid = (_l + _r) // 2
        if nums[_mid] == target:
            _start = _mid - 1
            _end = _mid + 1
            while _start >= 0 and nums[_start] == target:
                _start -= 1
            while _end < n and nums[_end] == target:
                _end += 1
            return [_start + 1, _end - 1]
        elif nums[_mid] < target:
            _l = _mid + 1
        else:
            _r = _mid - 1
    return [-1, -1]


#%%
def search_range_test():
    nums = [5, 7, 7, 8, 8, 10]
    target = 7
    result = search_range(nums, target)
    print(result)


search_range_test()


# %% [markdown]
# 81. Search in Rotated Sorted Array II (Medium)
# > https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/
# >一个原本增序的数组被首尾相连后按某个位置断开（如[1,2,2,3,4,5] ! [2,3,4,5,1,2]，在第一位和第二位断开），我们称其为旋转数组。给定一个值，判断这个值是否存在于这个旋转数组中。


def search(nums: list[int], target: int) -> bool:
    if not nums:
        return -1
    _l, _r = 0, len(nums) - 1
    while _l < _r:
        _mid = (_l + _r) // 2
        if nums[_mid] == target:
            return True
        if nums[_mid] <= nums[_r]:
            if target > nums[_mid] and target <= nums[_r]:
                _l = _mid + 1
            else:
                _r = _mid - 1
        else:
            if target < nums[_mid] and target >= nums[_r]:
                _r = _mid - 1
            else:
                _l = _mid + 1
    return False


# %%
def search_test():
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    print(search(nums, target))


search_test()

# %%
