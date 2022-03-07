# %% [markdown]
# ![20210709151338-2021-07-09-15-13-39](https://cdn.jsdelivr.net/gh/Gethin1990/PicBed/BlogImg/20210709151338-2021-07-09-15-13-39.png)
# ![20210709151309-2021-07-09-15-13-10](https://cdn.jsdelivr.net/gh/Gethin1990/PicBed/BlogImg/20210709151309-2021-07-09-15-13-10.png)

# 冒泡排序
# %%
# 不停交换，把最大的冒泡到最后面
def bubble_sort(nums: list[int]):
    n = len(nums)
    for _i in range(0, n - 1):
        for _j in range(0, n - 1 - _i):
            if nums[_j] > nums[_j + 1]:
                nums[_j], nums[_j + 1] = nums[_j + 1], nums[_j]
    return nums


def bubble_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    bubble_sort(nums)
    print(nums)


# 选择排序
# %%

# 最小的找出来，交换到最前面
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
        for _j in range(_i, 0, -1):
            if nums[_j] < nums[_j - 1]:
                nums[_j], nums[_j - 1] = nums[_j - 1], nums[_j]
            else:
                break
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


# %%
# 切成树，先序遍历
def quicksort2(array):
    if len(array) < 2:
        return array  # 基线条件：为空或只包含一个元素的数组是“有序”的
    else:
        pivot = array[0]  # 递归条件
        less = [i for i in array[1:] if i <= pivot]  # 由所有小于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]  # 由所有大于基准值的元素组成的子数组
        o_less = quicksort2(less)
        o_greater = quicksort2(greater)
    return o_less + [pivot] + o_greater


def quick_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    # quick_sort(nums, 0, len(nums) - 1)
    r = quicksort2(nums)
    print(r)


quick_sort_test()

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
    def init_heap(arr):
        n = len(arr)
        last_parent = (n - 1) // 2  # 最后一个parent节点
        for i in range(last_parent, -1, -1):
            adjust_heap(arr, n, i)

    def adjust_heap(arr, max_length, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        largest = parent

        if left < max_length and arr[left] > arr[largest]:
            largest = left
        if right < max_length and arr[right] > arr[largest]:
            largest = right
        if parent != largest:
            arr[parent], arr[largest] = arr[largest], arr[parent]
            adjust_heap(arr, max_length, largest)

    init_heap(arr)  # 初始化大顶堆
    for i in range(len(arr) - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 每次将最大值移到最后
        adjust_heap(arr, i, 0)
    return arr


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
