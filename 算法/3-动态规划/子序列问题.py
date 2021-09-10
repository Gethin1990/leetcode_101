# %% [markdown]
# 300. 最长递增子序列
# https://leetcode-cn.com/problems/longest-increasing-subsequence/

# %%
def length_of_list(nums: list[int]):
    if not nums:
        return 0
    dp = []
    for _i in range(len(nums)):
        dp.append(1)
        for _j in range(_i):
            if nums[_i] > nums[_j]:
                dp[_i] = max(dp[_i], dp[_j] + 1)
    return max(dp)


#%%
def length_of_list_test():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = length_of_list(nums)
    print(res)


length_of_list_test()

# %% [markdown]
# 1143. 最长公共子序列
# https://leetcode-cn.com/problems/longest-common-subsequence/

#%%
def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for _i in range(1, m + 1):
        for _j in range(1, n + 1):
            if text1[_i - 1] == text2[_j - 1]:
                dp[_i][_j] = dp[_i - 1][_j - 1] + 1
            else:
                dp[_i][_j] = max(dp[_i - 1][_j], dp[_i][_j - 1])
    return dp[m][n]


#%%
def longest_common_subsequence_test():
    text1 = "abc"
    text2 = "abcde"
    res = longest_common_subsequence(text1, text2)
    print(res)


longest_common_subsequence_test()


# %%
