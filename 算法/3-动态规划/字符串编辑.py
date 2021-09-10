# %% [markdown]
# 72. 编辑距离
# https://leetcode-cn.com/problems/edit-distance/

#%%
def min_distance(word1: str, word2: str):
    l1, l2 = len(word1), len(word2)

    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for _i1 in range(l1 + 1):
        dp[_i1][0] = _i1
    for _i2 in range(l2 + 1):
        dp[0][_i2] = _i2

    for _i1 in range(1, l1 + 1):
        for _i2 in range(1, l2 + 1):

            if word1[_i1 - 1] == word2[_i2 - 1]:
                dp[_i1][_i2] = dp[_i1 - 1][_i2 - 1]
            else:
                dp[_i1][_i2] = (
                    min(dp[_i1 - 1][_i2 - 1], dp[_i1 - 1][_i2], dp[_i1][_i2 - 1]) + 1
                )
    return dp[l1][l2]
#%%
def min_distance_test():
    word1 = "horse"
    word2 = "ros"
    result =min_distance(word1,word2)
    print(result)
min_distance_test()


# %% [markdown]
# 650. 只有两个键的键盘
# https://leetcode-cn.com/problems/2-keys-keyboard/

def min_steps(n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[-1]


# %% [markdown]
# 10. 正则表达式匹配
# https://leetcode-cn.com/problems/regular-expression-matching/

#%%
def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]  # 初始化
    dp[0][0] = True  # 空串匹配
    
    for j in range(1, n + 1):  # 初始化 p与空串的匹配，s不会以'*'打头，所以省略了一些，下同。
        dp[0][j] = dp[0][j-2] if p[j-1] == '*' else False  # 开头加了一位，则p中当前字符下标都要-1，s同。

    for i in range(1, m + 1):  # 开始填表
        for j in range(1, n + 1):
            if p[j-1] in {s[i-1], '.'}:  # p当前字符能匹配且不为*
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':  # p当前字符为 *
                if dp[i][j-2]:  # ‘*’匹配 0 次，看倒着数2位的位置
                    dp[i][j] = True 
                elif p[j-2] in {s[i-1], '.'}:  # ‘*’匹配一次或多次，看倒着数一位的位置
                    dp[i][j] = dp[i-1][j]
    return dp[m][n]

#%%
def is_match_test():
    s,p = "aaaa", "a*"
    r = is_match(s,p)
    print(r)
is_match_test()
# %%
