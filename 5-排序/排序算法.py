# %% [markdown]
# ![20210709151338-2021-07-09-15-13-39](https://cdn.jsdelivr.net/gh/Gethin1990/PicBed/BlogImg/20210709151338-2021-07-09-15-13-39.png)
# ![20210709151309-2021-07-09-15-13-10](https://cdn.jsdelivr.net/gh/Gethin1990/PicBed/BlogImg/20210709151309-2021-07-09-15-13-10.png)

# 冒泡排序
# %%
def bubble_sort(nums: list[int]):
    for i in range(len(nums)):
        is_sorted = True
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
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
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def selection_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    selection_sort(nums)
    print(nums)

# 插入排序


def insertion_sort(nums: list[int]):
    for i in range(1, len(nums)):
        pre_index = i-1
        current = nums[i]
        while pre_index >= 0 and current < nums[pre_index]:
            nums[pre_index+1] = nums[pre_index]
            pre_index -= 1
        nums[pre_index+1] = current
    return nums


def insertion_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    insertion_sort(nums)
    print(nums)


# 快速排序
# %%
def quick_sort(nums: list[int], l, r):
    if(l >= r):
        return
    low, high, = l, r
    key = nums[low]
    while(low < high):
        while(low < high and nums[high] >= key):
            high -= 1
        nums[low] = nums[high]
        while(low < high and nums[low] <= key):
            low += 1
        nums[high] = nums[low]
    nums[low] = key
    quick_sort(nums, l, low-1)
    quick_sort(nums, low+1, r)


def quick_sort_test():
    nums = [5, 4, 8, 9, 2, 7, 6]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)

# 归并排序
# %%


def merge(nums_1: list[int], nums_2: list[int]):
    sorted_arr = []
    idx_1, idx_2 = 0, 0
    while idx_1 < len(nums_1) and idx_2 < len(nums_2):
        if nums_1[idx_1] < nums_2[idx_2]:
            sorted_arr.append(nums_1[idx_1])
            idx_1 += 1
        else:
            sorted_arr.append(nums_2[idx_2])
            idx_2 += 1
    if idx_1 < len(nums_1):
        while idx_1 < len(nums_1):
            sorted_arr.append(nums_1[idx_1])
            idx_1 += 1
    if idx_2 < len(nums_2):
        while idx_2 < len(nums_2):
            sorted_arr.append(nums_2[idx_2])
            idx_2 += 1
    return sorted_arr


def merge_sort(nums: list[int]):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    arr_1, arr_2 = nums[:mid], nums[mid:]
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
    for i in range(len(arr)-1, 0, -1):
        # 依次将堆顶移至堆尾
        swap(arr, 0, i)
        heapLen -= 1
        heapify(arr, 0)
    return arr


def build_max_heap(arr):
    for i in range(len(arr)//2-1, -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if right < heapLen and arr[right] > arr[largest]:
        largest = right
    if left < heapLen and arr[left] > arr[largest]:
        largest = left
    if largest != i:
        swap(arr, largest, i)
        heapify(arr, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


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
