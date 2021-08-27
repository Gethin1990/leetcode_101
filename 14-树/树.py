TBD
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
# 110. 平衡二叉树
# https://leetcode-cn.com/problems/balanced-binary-tree/
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


# %% [markdown]
# 543. 二叉树的直径
# https://leetcode-cn.com/problems/diameter-of-binary-tree/

# %% [markdown]
# 437. 路径总和 III
# https://leetcode-cn.com/problems/path-sum-iii/

# %% [markdown]
# 101. 对称二叉树
# https://leetcode-cn.com/problems/symmetric-tree/

# %% [markdown]
# 1110. 删点成林
# https://leetcode-cn.com/problems/delete-nodes-and-return-forest/

# %% [markdown]
# 637. 二叉树的层平均值
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/


# %% [markdown]
# 105. 从前序与中序遍历序列构造二叉树
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# %% [markdown]
# 144. 二叉树的前序遍历
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/


# %% [markdown]
# 99. 恢复二叉搜索树
# https://leetcode-cn.com/problems/recover-binary-search-tree/

# %% [markdown]
# 669. 修剪二叉搜索树
# https://leetcode-cn.com/problems/trim-a-binary-search-tree/
# %% [markdown]
# 208. 实现 Trie (前缀树)
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/

# %% [markdown]
# 208. 实现 Trie (前缀树)
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/
