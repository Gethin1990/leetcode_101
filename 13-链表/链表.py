# %%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 增加哨兵节点，
def build_list(count: int) -> ListNode:
    i = 0
    sentinel = ListNode(0)
    l = ListNode(0)
    sentinel.next = l
    _curr = l
    while _curr:
        if i == count:
            break
        i += 1
        _curr.next = ListNode(i)
        _curr = _curr.next

    li = sentinel.next
    return li


def print_list(l: ListNode):
    while l:
        print(l.val)
        l = l.next


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
    anchor = reverse_list(node.next)
    b_node = node.next
    b_node.next = node
    node.next = None
    return anchor


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

# setps:
# 1. 递归框架 + 返回条件
# 2. 画 递归树 
# 3. 递：node.next.next 但结合返回条件，实际递归树中递入的是 1，3，5，none
# 4. 归：b_node(node.next) 函数计算后的结果 为 6，4，2
# 5. 断链与重链

#%%
def swap_pairs(node: ListNode) -> ListNode:
    if not node or not node.next:
        return node
    last = swap_pairs(node.next.next)
    b_node = node.next

    node.next = last
    b_node.next = node
    return b_node


#%%
def swap_test():
    list = build_list(6).next
    res = swap_pairs(list)
    print_list(res)


swap_test()

# %%
