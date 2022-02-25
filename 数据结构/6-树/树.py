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
    print(root.val, l_high, r_high, deep)
    return deep


# %%
def max_depth_test():
    tree = Tree()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
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
        if l_height == -1 or r_height == -1 or abs(l_height - r_height) > 1:
            return -1
        return 1 + max(l_height, r_height)

    return height(root) >= 0


# %% [markdown]
# 543. 二叉树的直径
# https://leetcode-cn.com/problems/diameter-of-binary-tree/

#%%
def diameter_of_binary_tree(root: TreeNode) -> int:
    maxtemp = 1

    def dfs(node: TreeNode):
        if not node:
            return 0
        L = dfs(node.left)
        R = dfs(node.right)
        nonlocal maxtemp
        maxtemp = max(L + R, maxtemp)
        return max(L, R) + 1

    dfs(root)
    return maxtemp


#%%
def diameter_of_binary_tree_test():
    tree = Tree()
    arr = [1, 2, 3, 4, 5]
    for val in arr:
        tree.add(val)
    result = diameter_of_binary_tree(tree.root)
    print(result)


diameter_of_binary_tree_test()


# %% [markdown]
# 437. 路径总和 III
# https://leetcode-cn.com/problems/path-sum-iii/

#%%
def path_sum(root: TreeNode, sum: int) -> int:
    if not root:
        return 0
    n = 0

    def dfs(node: TreeNode, sum: int):
        if not node:
            return 0
        if node.val is None:
            node.val = 0

        sum -= node.val
        count = 1 if sum == 0 else 0
        l_o = dfs(node.left, sum)
        r_o = dfs(node.right, sum)
        count += l_o + r_o
        return count

    n_o = dfs(root, sum)
    l_o = path_sum(root.left, sum)
    r_o = path_sum(root.right, sum)
    n += n_o + l_o + r_o
    return n


#%%
def path_sum_test():
    tree = Tree()
    root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    for val in root:
        tree.add(val)
    targetSum = 8
    result = path_sum(tree.root, targetSum)
    print(result)


path_sum_test()


# %% [markdown]
# 101. 对称二叉树
# https://leetcode-cn.com/problems/symmetric-tree/

#%%
def is_symmetric(root: TreeNode):
    def check(p: TreeNode, q: TreeNode):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        o_1 = check(p.left, q.right)
        o_2 = check(p.right, q.left)
        return (p.val is q.val) and o_1 and o_2

    return check(root, root)


#%%
def is_symmetric_test():
    tree = Tree()
    root = [1, 2, 2, 3, 4, 4, 3]
    for val in root:
        tree.add(val)
    result = is_symmetric(tree.root)
    print(result)


is_symmetric_test()

# %% [markdown]
# 1110. 删点成林
# https://leetcode-cn.com/problems/delete-nodes-and-return-forest/

#%%
def delete_nodes(root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
    if not root:
        return None
    mapper = set(to_delete)
    ans = [] if root.val in mapper else [root]

    def dfs(node, parent, direction):
        if not node:
            return
        dfs(node.left, node, "left")
        dfs(node.right, node, "right")
        if node.val in mapper:
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
            if direction == "left":
                parent.left = None
            if direction == "right":
                parent.right = None

    dfs(root, None, None)
    return ans


#%%
def delete_nodes_test():
    tree = Tree()
    arr = [1, 2, 3, 4, 5, 6, 7]
    for val in arr:
        tree.add(val)
    to_delete = [3, 5]
    result = delete_nodes(tree.root, to_delete)
    for item in result:
        print(tree.travel(item))


delete_nodes_test()

# %% [markdown]
# 637. 二叉树的层平均值
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/

#%%
def average_of_levels(root: TreeNode):
    totals = []
    counts = []

    def dfs(node, depth):
        if node is None or node.val is None:
            return
        print(depth)
        # 递归下一次第一个元素
        if depth >= len(totals):
            totals.append(node.val)
            counts.append(1)
        # 递归下一次非第一个元素
        else:
            totals[depth] += node.val
            counts[depth] += 1
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return [total / count for total, count in zip(totals, counts)]


#%%
def average_of_levels_test():
    tree = Tree()
    arr = [1,2,3,4,5]
    for val in arr:
        tree.add(val)
    result = average_of_levels(tree.root)
    print(result)


average_of_levels_test()


# %% [markdown]
# 105. 从前序与中序遍历序列构造二叉树
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#%%
def build_tree(pre_order: list[int], in_order: list[int]) -> TreeNode:
    if not pre_order or not in_order:
        return None
    root = TreeNode(pre_order[0])
    idx = in_order.index(pre_order[0])
    root.left = build_tree(pre_order[1 : 1 + idx], in_order[:idx])
    root.right = build_tree(pre_order[1 + idx :], in_order[idx + 1 :])
    return root


#%%
def build_tree_test():
    pre_order = [3, 9, 20, 15, 7]
    in_order = [9, 3, 15, 20, 7]
    tree = Tree()
    result = build_tree(pre_order, in_order)
    print(tree.travel(result))


build_tree_test()


# %% [markdown]
# 144. 二叉树的前序遍历
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

#%%
def preorder_traversal(root: TreeNode) -> list[int]:
    def preorder(root: TreeNode):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)

    res = list()
    preorder(root)
    return res


#%%
def preorder_traversal_test():
    tree = Tree()
    arr = [1, 2, 3, 4, 5, 6, 7]
    for val in arr:
        tree.add(val)
    result = preorder_traversal(tree.root)
    print(result)


preorder_traversal_test()

# TBD
# %% [markdown]
# 99. 恢复二叉搜索树
# https://leetcode-cn.com/problems/recover-binary-search-tree/

# steps:
# 1. 中序遍历，生成数组
# 2. 遍历结果，找出可能错误得交换点
# 3. 如果错误得交换点不为空，交换

#%%
def recover_tree(root: TreeNode):
    # 中序遍历二叉树，将遍历结果保存到列表中
    node = []

    def dfs(root):
        if root == None:
            return
        dfs(root.left)
        node.append(root)
        dfs(root.right)

    dfs(root)

    x, y = None, None
    pre = node[0]
    # 循环遍历，找到错误交换的x,y
    for i in range(1, len(node)):
        if pre.val > node[i].val:
            y = node[i]
            # 记录第一个出现的交换值
            if not x:
                x = pre
        pre = node[i]

    # 将找到的x和y进行交换
    if x and y:
        x.val, y.val = y.val, x.val


#%%
def recover_tree_test():
    tree = Tree()
    arr = [7, 2, 6, 1, 3, 5, 4]
    for val in arr:
        tree.add(val)
    recover_tree(tree.root)
    print(tree.travel(tree.root))


recover_tree_test()


# %% [markdown]
# 669. 修剪二叉搜索树
# https://leetcode-cn.com/problems/trim-a-binary-search-tree/

#%%
def trim_BST(root, L, R) -> TreeNode:
    def trim(node):
        if not node or node.val is None:
            return None
        elif node.val > R:
            return trim(node.left)
        elif node.val < L:
            return trim(node.right)
        else:
            node.left = trim(node.left)
            node.right = trim(node.right)
            return node

    return trim(root)


#%%
def trim_BST_test():
    tree = Tree()
    arr = [3, 0, 4, None, 2, None, None, None, None, 1, None]
    for val in arr:
        tree.add(val)
    result = trim_BST(tree.root, 1, 3)
    print(tree.travel(result))


trim_BST_test()

# %% [markdown]
# 208. 实现 Trie (前缀树)
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/

#%%
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def __searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.__searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.__searchPrefix(prefix) is not None


#%%
def trie_test():
    trie = Trie()
    trie.insert("apple")
    r1 = trie.search("apple")
    r2 = trie.search("app")
    r3 = trie.startsWith("app")
    trie.insert("app")
    r4 = trie.search("app")
    print(r1, r2, r3, r4)


trie_test()

# %%
