#%%
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self) -> None:
        self.root = None

    def add(self, item):
        node = TreeNode(item)

        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while q:
                point = q.pop(0)
                if point.left is None:
                    point.left = node
                    return
                if point.right is None:
                    point.right = node
                    return
                else:
                    q.append(point.left)
                    q.append(point.right)

    def travel(self, root: TreeNode):
        if root is None:
            return []
        arr = []
        q = []
        q.append(root)
        while q:
            point = q.pop(0)
            arr.append(point.val)
            if point.left:
                q.append(point.left)
            if point.right:
                q.append(point.right)
        return arr


#%%
def tree_test():
    tree = Tree()
    arr = [1, 2, 3, 4, 5]
    for val in arr:
        tree.add(val)
    print(tree.travel(tree.root))


tree_test()


# %%
def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    l_high = max_depth(root.left)
    r_high = max_depth(root.right)
    deep = max(l_high, r_high) + 1
    return deep


# %%
def max_depth_test():
    tree = Tree()
    arr = [1, 2, 3, 4, 5]
    for val in arr:
        tree.add(val)
    res = max_depth(tree.root)
    print(res)


max_depth_test()

# %% [markdown]
# 110
def is_balanced(root: TreeNode) -> bool:
    def height(root) -> int:
        if not root:
            return 0
        l_height = height(root.left)
        r_height = height(root.right)
        if l_height == -1 or r_height == -1 or abs(l_height, r_height) > 1:
            return -1
        return 1 + max(l_height, r_height)

    return height(root) >= 0
