# %% [markdown]
# ![20210709151338-2021-07-09-15-13-39](https://cdn.jsdelivr.net/gh/Gethin1990/PicBed/BlogImg/20210709151338-2021-07-09-15-13-39.png)
# ![20210709151309-2021-07-09-15-13-10](https://cdn.jsdelivr.net/gh/Gethin1990/PicBed/BlogImg/20210709151309-2021-07-09-15-13-10.png)

# 冒泡排序
# %%
def bubble_sort(nums: list[int]):
    for _i in range(len(nums)):
        is_sorted = True
        for _j in range(len(nums) - 1 - _i):
            if nums[_j] > nums[_j + 1]:
                nums[_j], nums[_j + 1] = nums[_j + 1], nums[_j]
                is_sorted = False
        if is_sorted:
            break
    return nums


def bubble_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    bubble_sort(nums)
    print(nums)


# 选择排序
# %%


def selection_sort(nums: list[int]):
    for _i in range(len(nums) - 1):
        _min_index = _i
        for _j in range(_i + 1, len(nums)):
            if nums[_j] < nums[_min_index]:
                _min_index = _j
            if _min_index != _i:
                nums[_i], nums[_min_index] = nums[_min_index], nums[_i]
    return nums


def selection_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    selection_sort(nums)
    print(nums)


# 插入排序
# %%
def insertion_sort(nums: list[int]):
    for _i in range(1, len(nums)):
        _pre_index = _i - 1
        current = nums[_i]
        while _pre_index >= 0 and current < nums[_pre_index]:
            nums[_pre_index + 1] = nums[_pre_index]
            _pre_index -= 1
        nums[_pre_index + 1] = current
    return nums


def insertion_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    insertion_sort(nums)
    print(nums)


# 快速排序
# %%
def quick_sort(nums: list[int], _l, _r):
    if _l >= _r:
        return
    _low, _high, = (
        _l,
        _r,
    )
    key = nums[_low]
    while _low < _high:
        while _low < _high and nums[_high] >= key:
            _high -= 1
        nums[_low] = nums[_high]
        while _low < _high and nums[_low] <= key:
            _low += 1
        nums[_high] = nums[_low]
    nums[_low] = key
    quick_sort(nums, _l, _low - 1)
    quick_sort(nums, _low + 1, _r)


def quick_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)


# 归并排序
# %%


def merge(nums_1: list[int], nums_2: list[int]):
    sorted_arr = []
    _idx_1, _idx_2 = 0, 0
    while _idx_1 < len(nums_1) and _idx_2 < len(nums_2):
        if nums_1[_idx_1] < nums_2[_idx_2]:
            sorted_arr.append(nums_1[_idx_1])
            _idx_1 += 1
        else:
            sorted_arr.append(nums_2[_idx_2])
            _idx_2 += 1
    if _idx_1 < len(nums_1):
        while _idx_1 < len(nums_1):
            sorted_arr.append(nums_1[_idx_1])
            _idx_1 += 1
    if _idx_2 < len(nums_2):
        while _idx_2 < len(nums_2):
            sorted_arr.append(nums_2[_idx_2])
            _idx_2 += 1
    return sorted_arr


def merge_sort(nums: list[int]):
    if len(nums) <= 1:
        return nums
    _mid = len(nums) // 2
    arr_1, arr_2 = nums[:_mid], nums[_mid:]
    return merge(merge_sort(arr_1), merge_sort(arr_2))


def merge_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    merge_sort(nums)
    print(nums)


# 堆排序
# %%


def heap_sort(arr):
    global heapLen
    # 用于标记堆尾部的索引
    heapLen = len(arr)
    # 构建最大堆
    build_max_heap(arr)
    for _i in range(len(arr) - 1, 0, -1):
        # 依次将堆顶移至堆尾
        swap(arr, 0, _i)
        heapLen -= 1
        heapify(arr, 0)
    return arr


def build_max_heap(arr):
    for _i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, _i)


def heapify(arr, _i):
    _left = 2 * _i + 1
    _right = 2 * _i + 2
    _largest = _i
    if _right < heapLen and arr[_right] > arr[_largest]:
        _largest = _right
    if _left < heapLen and arr[_left] > arr[_largest]:
        _largest = _left
    if _largest != _i:
        swap(arr, _largest, _i)
        heapify(arr, _largest)


def swap(arr, _i, _j):
    arr[_i], arr[_j] = arr[_j], arr[_i]


def heap_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    heap_sort(nums)
    print(nums)


# %%
bubble_sort_test()
selection_sort_test()
insertion_sort_test()
quick_sort_test()
merge_sort_test()
heap_sort_test()
# %%
