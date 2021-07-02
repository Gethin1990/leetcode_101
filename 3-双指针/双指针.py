
# %% [markdown]
# # 双指针

# %%
import collections
from typing import List

# %% [markdown]
#  167. Two Sum II - Input array is sorted (Easy)
#  >在一个增序的整数数组里找到两个数，使它们的和为给定值。已知有且只有一对解。

# %%


def two_sum(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers)-1
    while l < r:
        num_sum = numbers[l]+numbers[r]
        if num_sum == target:
            break
        if num_sum < target:
            l += 1
        else:
            r -= 1
    return [l+1, r+1]


def two_sum_test():
    result = two_sum([2, 7, 11, 15], 9)
    print(result)

# %% [markdown]
#  88. Merge Sorted Array (Easy)
#  >给定两个有序数组，把两个数组合并为一个


def merge(num1: list[int], m: int, num2: list[int], n: int):
    p1, p2 = m - 1, n - 1
    tail = m + n - 1
    while p1 >= 0 or p2 >= 0:
        if p1 == -1:
            num1[tail] = num2[p2]
            p2 -= 1
        elif p2 == -1:
            num1[tail] = num1[p1]
            p1 -= 1
        elif num1[p1] > num2[p2]:
            num1[tail] = num1[p1]
            p1 -= 1
        else:
            num1[tail] = num2[p2]
            p2 -= 1
        tail -= 1


def merge_test():
    num1 = [1, 2, 3, 0, 0, 0]
    num2 = [2, 5, 6]
    merge(num1, 3, num2, 3)
    print(num1)

# %% [markdown]
#  142. Linked List Cycle II (Medium)
#  >给定一个链表，如果有环路，找出环路的开始点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(head: ListNode) -> ListNode:
    slow, fast = head, head
    while True:
        if fast == None or fast.next == None:
            return
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            break
    fast = head
    while fast != slow:
        fast, slow = fast.next, slow.next
    return fast

# %%


def detect_cycle_test():
    data = [3, 2, 0, -4]
    tail = head = ListNode(data[0])
    for x in data[1:]:
        tail.next = ListNode(x)  # Create and add another node
        tail = tail.next  # Move the tail pointer
    tail.next = head.next
    result = detect_cycle(head)
    print(result.val)



# %% [markdown]
#  76. MinimumWindow Substring (Hard)
#  >给定两个字符串S 和T，求S 中包含T 所有字符的最短连续子字符串的长度，同时要求时间复杂度不得超过O(n)。

# %%
def min_window(s: str, t: str) -> str:
    need = collections.defaultdict(int)
    for c in t:
        need[c] += 1
    needCnt = len(t)
    i = 0
    res = (0, float('inf'))
    for j, c in enumerate(s):
        if need[c] > 0:
            needCnt -= 1
        need[c] -= 1
        if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
            while True:  # 步骤二：增加i，排除多余元素
                c = s[i]
                if need[c] == 0:
                    break
                need[c] += 1
                i += 1
            if j-i < res[1]-res[0]:  # 记录结果
                res = (i, j)
            need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
            needCnt += 1
            i += 1
    # 如果res始终没被更新过，代表无满足条件的结果
    return '' if res[1] > len(s) else s[res[0]:res[1]+1]

# %%
def min_window_test():
    s="DOABECODEBANC"
    t="ABC"
    result = min_window(s,t)
    print(result)


# %%
# two_sum_test()
# merge_test()
# detect_cycle_test()

min_window_test()
# %%
