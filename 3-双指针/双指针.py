# %% [markdown]
# # 双指针

# %% [markdown]
# 167. Two Sum II - Input array is sorted (Easy)
# >在一个增序的整数数组里找到两个数，使它们的和为给定值。已知有且只有一对解。

# %%


def two_sum(numbers: list[int], target: int) -> list[int]:
    _l = 0
    _r = len(numbers) - 1
    while _l < _r:
        num_sum = numbers[_l] + numbers[_r]
        if num_sum == target:
            break
        if num_sum < target:
            _l += 1
        else:
            _r -= 1
    return [_l + 1, _r + 1]


# %%
def two_sum_test():
    result = two_sum([2, 7, 11, 15], 9)
    print(result)


two_sum_test()

# %% [markdown]
# 88. Merge Sorted Array (Easy)
# >给定两个有序数组，把两个数组合并为一个


def merge(num1: list[int], m: int, num2: list[int], n: int):
    _p1, _p2 = m - 1, n - 1
    _tail = m + n - 1
    while _p1 >= 0 or _p2 >= 0:
        if _p1 == -1:
            num1[_tail] = num2[_p2]
            _p2 -= 1
        elif _p2 == -1:
            num1[_tail] = num1[_p1]
            _p1 -= 1
        elif num1[_p1] > num2[_p2]:
            num1[_tail] = num1[_p1]
            _p1 -= 1
        else:
            num1[_tail] = num2[_p2]
            _p2 -= 1
        _tail -= 1


# %%
def merge_test():
    num1 = [1, 2, 3, 0, 0, 0]
    num2 = [2, 5, 6]
    merge(num1, 3, num2, 3)
    print(num1)


merge_test()

# %% [markdown]
# 142. Linked List Cycle II (Medium)
# >给定一个链表，如果有环路，找出环路的开始点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(head: ListNode) -> ListNode:
    _slow, _fast = head, head
    while True:
        if _fast == None or _fast.next == None:
            break
        _fast, _slow = _fast.next.next, _slow.next
        if _fast == _slow:
            break
    _fast = head
    while _fast != _slow:
        _fast, _slow = _fast.next, _slow.next
    return _fast


# %%
def detect_cycle_test():
    data = [3, 2, 0, -4]
    _tail = _head = ListNode(data[0])
    for x in data[1:]:
        _tail.next = ListNode(x)  # Create and add another node
        _tail = _tail.next  # Move the tail pointer
    _tail.next = _head.next
    result = detect_cycle(_head)
    print(result.val)


detect_cycle_test()

# %% [markdown]
#  76. MinimumWindow Substring (Hard)
#  >给定两个字符串S 和T，求S 中包含T 所有字符的最短连续子字符串的长度，同时要求时间复杂度不得超过O(n)。

# %%
import collections


def min_window(s: str, t: str) -> str:
    need = collections.defaultdict(int)
    for c in t:
        need[c] += 1
    need_cnt = len(t)
    _i = 0
    res = (0, float("inf"))
    for _j, c in enumerate(s):
        if need[c] > 0:
            need_cnt -= 1
        need[c] -= 1
        if need_cnt == 0:  # 步骤一：滑动窗口包含了所有T元素
            while True:  # 步骤二：增加i，排除多余元素
                c = s[_i]
                if need[c] == 0:
                    break
                need[c] += 1
                _i += 1
            if _j - _i < res[1] - res[0]:  # 记录结果
                res = (_i, _j)
            need[s[_i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
            need_cnt += 1
            _i += 1
    # 如果res始终没被更新过，代表无满足条件的结果
    return "" if res[1] > len(s) else s[res[0] : res[1] + 1]


# %%
def min_window_test():
    s = "ADOBECODEBANC"
    t = "ABC"
    result = min_window(s, t)
    print(result)


min_window_test()
# %%
