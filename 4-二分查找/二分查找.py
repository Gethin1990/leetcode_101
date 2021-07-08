# %% [markdown]
#  69. Sqrt(x) (Easy)
#  >给定一个非负整数，求它的开方，向下取整。


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


def my_sqrt_test():
    result = my_sqrt(8)
    print(result)

# %% [markdown]
#  34. Find First and Last Position of Element in Sorted Array (Medium)
#  >给定一个增序的整数数组和一个值，查找该值第一次和最后一次出现的位置。


def search_range(nums: list[int], target: int) -> list[int]:
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


def search_range_test():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    result = search_range(nums, target)
    print(result)


# %% [markdown]
#  81. Search in Rotated Sorted Array II (Medium)
#  >一个原本增序的数组被首尾相连后按某个位置断开（如[1,2,2,3,4,5] ! [2,3,4,5,1,2]，在第一位和第二位断开），我们称其为旋转数组。给定一个值，判断这个值是否存在于这个旋转数组中。

def search(nums: list[int], target: int) -> bool:
    if not nums:
        return -1
    l, r = 0, len(nums)-1
    while l < r:
        mid = (l+r)//2
        if nums[mid] == target:
            return True
        if nums[mid] <= nums[r]:
            if target > nums[mid] and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] and target >= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return False


def search_test():
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    print(search(nums, target))


# %%
my_sqrt_test()
search_range_test()
search_test()

# %%
