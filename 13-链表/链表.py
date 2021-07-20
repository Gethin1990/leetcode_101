# %%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(count: int) -> ListNode:
    i = 0
    sentinel = ListNode(0)
    l = ListNode(0)
    sentinel.next = l
    _prev, _curr = sentinel, l
    while _curr:
        if i == count:
            break
        i += 1
        _curr.next = ListNode(i)
        _prev = _curr
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
# %%


