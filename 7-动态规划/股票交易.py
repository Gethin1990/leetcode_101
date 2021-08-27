# %% [markdown]
# 121. 买卖股票的最佳时机
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

#%%
def max_profit(prices: list[int]):
    # 下标含义：i=days ; j-0:持有/买入,j-1:持有：卖出
    days = len(prices)
    if days == 0:
        return 0
    # DP初始
    dp = [[0] * 2 for _ in range(days)]
    dp[0][0] = -prices[0]
    dp[0][1] = 0

    # 循环顺序
    for _i in range(1, days):
        # DP推导
        dp[_i][0] = max(dp[_i - 1][0], -prices[_i])
        dp[_i][1] = max(dp[_i - 1][1], prices[_i] + dp[_i - 1][0])

    # 打印DP
    return dp[-1][1]


#%%
def max_profit_test():
    prices = [7, 1, 5, 3, 6, 4]
    result = max_profit(prices)
    print(result)


max_profit_test()

# %% [markdown]
# 188. 买卖股票的最佳时机 IV
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

#%%
def max_profit(k: int, prices: list[int]):
    days = len(prices)
    if days == 0:
        return 0

    # 下标含义：i= days, j = 第i天的状态 k笔交易 j<2*k+1
    # DP初始
    dp = [[0] * (2 * k + 1) for _ in range(days)]
    for _j in range(1, 2 * k, 2):
        dp[0][_j] = -prices[0]
    # 循坏顺序
    for _i in range(1, len(prices)):
        # DP 推导
        for _j in range(0, 2 * k - 1, 2):
            dp[_i][_j + 1] = max(dp[_i - 1][_j + 1], dp[_i - 1][_j] - prices[_i])
            dp[_i][_j + 2] = max(dp[_i - 1][_j + 2], dp[_i - 1][_j + 1] + prices[_i])
    # 打印DP
    return dp[-1][2 * k]


#%%
def max_profit_test():
    prices = [3, 2, 6, 5, 0, 3]
    result = max_profit(2, prices)
    print(result)


max_profit_test()

# %% [markdown]
# 309. 最佳买卖股票时机含冷冻期
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

#%%
def max_profit(prices: list[int]) -> int:
    n = len(prices)
    if n == 0:
        return 0
    dp = [[0] * 4 for _ in range(n)]
    dp[0][0] = -prices[0]  # 持股票
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3], dp[i - 1][1]) - prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
        dp[i][2] = dp[i - 1][0] + prices[i]
        dp[i][3] = dp[i - 1][2]
    return max(dp[n - 1][3], dp[n - 1][1], dp[n - 1][2])


#%%
def max_profit_test():
    prices = [1, 2, 3, 0, 2]
    result = max_profit(prices)
    print(result)


max_profit_test()
# %%
