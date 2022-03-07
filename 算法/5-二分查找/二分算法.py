# 基本二分搜索
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 直接返回
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 直接返回
    return -1


# 寻找左侧边界的二分搜索，开区间写法
def left_bound(nums, target):
    left, right = 0, len(nums)
    if right == 0:
        return -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定左侧边界
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 检查left越界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


# 寻找右侧边界的二分搜索，开区间写法
def right_bound(nums, target):
    left, right = 0, len(nums)
    if right == 0:
        return -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定右侧边界
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 检查越界情况
    if left == 0 or nums[left - 1] != target:
        return -1
    return left - 1


# 寻找左侧边界的二分搜索，闭区间写法
def left_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定左侧边界
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 检查left越界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


# %%
# 寻找右侧边界的二分搜索，闭区间写法
def right_bound(nums, target):
    left, right = 0, len(nums) - 1  # 1. 闭区间
    while left <= right:  # 2. 对齐下标
        mid = (left + right) // 2  # 3. 二分
        if nums[mid] == target:
            # 4.if<t:{left = mid+1}; if>t:{right = mid+1};if==t:{left+1}
            left = mid + 1  # 锁定右侧边界
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1
    # 检查right越界情况
    if right < 0 or nums[right] != target:  # 5. 检查越界情况
        return -1
    return right  # 6. 返回下界标


#%%
def binary_search_re(nums, target):
    left, right = 0, len(nums) - 1

    def re_fn(left, right, target):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            o = re_fn(mid + 1, right, target)
        if nums[mid] > target:
            o = re_fn(left, mid - 1, target)
        return o

    return re_fn(left, right, target)


#%%
def test():
    nums = [0, 3, 4, 5, 6, 7]
    target = 0
    r = binary_search_re(nums, target)
    print(r)


test()
# %%
