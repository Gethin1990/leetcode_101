# %%
from _typeshed import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

# %%
def reverse_list(node: ListNode) -> ListNode:
    if not node.next:
        return node
    new_node = reverse_list(node.next)
    node.next.next = node
    node.next = None
    return new_node


# %%
def reverse_list_test():
    node = build_list(10)
    new_node = reverse_list(node)
    print_list(new_node)


reverse_list_test()


# %% [markdown]
# 206. 反转链表
# >https://leetcode-cn.com/problems/merge-two-sorted-lists/
# >将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


# %%
def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        l1.next = merge_two_list(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_list(l1, l2.next)
        return l2


# %%
def merge_two_list_test():
    l1 = build_list(5)
    l2 = build_list(10)
    res = merge_two_list(l1,l2)
    print_list(res)
merge_two_list_test()
# %%
