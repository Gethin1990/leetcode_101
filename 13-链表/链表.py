# %%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 增加哨兵节点，
def build_list(count: int) -> ListNode:
    i = 0
    sentinel = ListNode(0)
    node = ListNode(0)
    sentinel.next = node
    _current = node
    while _current:
        if i == count:
            break
        i += 1
        _current.next = ListNode(i)
        _current = _current.next

    li = sentinel.next
    return li


def print_list(l: ListNode):
    while l:
        print(l.val)
        l = l.next

def revers_list(node: ListNode) -> ListNode:
    _pre, _current = None, node
    while _current:
        _next = _current.next
        _current.next = _pre  # 链接
        _pre = _current  # 移动指针
        _current = _next
    return _pre



# %% [markdown]
# 206. 反转链表
# >https://leetcode-cn.com/problems/reverse-linked-list/
# >给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# steps:
# 1. 递归框架+退出条件
# 2. 递：无操作，归：新链+断链
# %%
def reverse_list(node: ListNode) -> ListNode:
    if not node.next:
        return node
    _last = reverse_list(node.next)
    _next, _curr = node.next, node
    _next.next = node
    _curr.next = None
    return _last


def revers_list_2(node: ListNode) -> ListNode:
    _pre, _curr = None, node
    while _curr:
        _next = _curr.next
        _curr.next = _pre  # 链接
        _pre = _curr  # 移动指针
        _curr = _next
    return _pre


# %%
def reverse_list_test():
    node = build_list(4).next
    new_node = reverse_list(node)
    print_list(new_node)


reverse_list_test()


# %% [markdown]
# 21. 合并两个有序链表
# >https://leetcode-cn.com/problems/merge-two-sorted-lists/
# >将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# steps:
# 1. 递归框架 + 退出条件
# 2. 例：递：判断 val 条件 if l1.val>=l2.val 递 l2.next ，归:因为递进的是l2 return l2

# %%
def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val >= l2.val:
        l2.next = merge_two_list(l1, l2.next)
        return l2
    else:
        l1.next = merge_two_list(l1.next, l2)
        return l1


# %%
def merge_two_list_test():
    l1 = build_list(5)
    l2 = build_list(10)
    res = merge_two_list(l1, l2)
    print_list(res)


merge_two_list_test()
# %%

# %% [markdown]
# 24. 两两交换链表中的节点
# >https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# >给定一个矩阵，交换每个相邻的一对节点

# steps:
# 1. 递归框架 + 返回条件
# 2. 画 递归树
# 3. 递：node.next.next 但结合返回条件，实际递归树中递入的是 1，3，5，none
# 4. 归：b_node(node.next) 函数计算后的结果 为 6，4，2
# 5. 断链与重链

#%%
def swap_pairs(node: ListNode) -> ListNode:
    if not node or not node.next:
        return node
    _last = swap_pairs(node.next.next)
    _next = node.next

    node.next = _last
    _next.next = node
    return _next


#%%
def swap_test():
    list = build_list(6).next
    res = swap_pairs(list)
    print_list(res)


swap_test()

# %%

# %% [markdown]
# 160. 相交链表
# >https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# >给定两个链表，判断它们是否相交于一点，并求这个相交节点

# %%
def get_intersection_node(node1: ListNode, node2: ListNode) -> ListNode:
    if node1 is None or node2 is None:
        return None
    _l1, _l2 = node1, node2
    while _l1 != _l2:
        _l1 = _l1.next if _l1 else node2
        _l2 = _l2.next if _l2 else node1
    return _l1


# %%
def get_intersection_node_test():
    l1 = build_list(3)
    l2 = build_list(2)
    l3 = build_list(2).next

    l1.next.next.next.next = l3
    l2.next.next.next = l3

    res = get_intersection_node(l1, l2)
    print(res.val if res else "None")


get_intersection_node_test()

# %%


# %% [markdown]
# 234. 回文链表
# https://leetcode-cn.com/problems/palindrome-linked-list/
# >请判断一个链表是否为回文链表。

# %%
def is_palindrome(node: ListNode) -> bool:
    values = []
    _curr = node
    while _curr is not None:
        values.append(_curr.val)
        _curr = _curr.next
    return values == values[::-1]

# %%
def is_palindrome_test():
    l1 = build_list(3)
    l2 = build_list(3)
    l2 = revers_list(l2)
    l1.next.next.next.next = l2
    res = is_palindrome(l1)
    print(res)
is_palindrome_test()

# %%
