# %% [markdown]
# 279. 完全平方数
# >https://leetcode-cn.com/problems/perfect-squares/
# >给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

# steps:
# 1. def def dp[n+1] float('inf')
# 2. dp[0]=0
# 3. dp[i] = min(dp[i],dp[i-j*j]+1)

# %%
import math


def num_squares(n: int) -> int:
    dp = [0] + [float("inf")] * n
    rg = int(math.sqrt(n))
    for _j in range(1, rg + 1):
        for _i in range(_j * _j, n + 1):
            dp[_i] = min(dp[_i], dp[_i - _j * _j] + 1)
    return dp[n]


# %%
def num_squares_test():
    n = 12
    res = num_squares(n)
    print(res)


num_squares_test()

# %% [markdown]
# 91. 解码方法
# >https://leetcode-cn.com/problems/decode-ways/
# >已知字母A-Z 可以表示成数字1-26。给定一个数字串，求有多少种不同的字符串等价于这个数字串。

# steps:
# 1. def dp[n+1] 0
# 2. dp[0]=1
# 3. Scenario 1：取一个数字s1(s[i-1])，这个数字s1不可能是0， 并且在字母i之内
# 4. Scenario 2：取两个数字s2(s[i-2],s[i-1]), 组成字母，这个字母只能在j-z，两位数必然<=26 & 前数字dp[i-2]不能为0

# %%
def num_decodings(s: str) -> int:
    n = len(s)
    dp = [1] + [0] * n
    for _i in range(1, n + 1):
        if s[_i - 1] != "0":
            dp[_i] += dp[_i - 1]
        if _i > 1 and s[_i - 2] != "0" and int(s[_i - 2 : _i]) <= 26:
            dp[_i] += dp[_i - 2]
    return dp[n]


# %%
def num_decodings_test():
    s = "226"
    res = num_decodings(s)
    print(res)


num_decodings_test()

# %%

# %% [markdown]
# 139. 单词拆分
# >https://leetcode-cn.com/problems/word-break/
# >给定一个字符串和一个字符串集合，求是否存在一种分割方式，使得原字符串分割后的子字符串都可以在集合内找到。

# %%
def word_break(s: str, wordDict: list[str]) -> bool:
    n = len(s)
    dp = [True] + [False] * n
    for _i in range(n):
        for _j in range(_i + 1, n + 1):
            if dp[_i] and (s[_i:_j] in wordDict):
                dp[_j] = True

    return dp[n]

# %%
def wordBreak_test():
    s = "leetcode"
    wordDict = ["leet", "code"]
    res = word_break(s,wordDict)
    print(res)
wordBreak_test()



# %%
