# %% [markdown]
# 416. 分割等和子集
# https://leetcode-cn.com/problems/partition-equal-subset-sum/

#%%
def can_partition(numbers: list[int]):
    n = len(numbers)
    if n < 2:
        return False

    total = sum(numbers)
    # if total 是奇数，肯定不满足条件
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [True] + [False] * target
    for _, num in enumerate(numbers):
        for _j in range(target, num - 1, -1):
            dp[_j] = dp[_j - num]
    return dp[target]


#%%
def can_partition_test():
    numbers = [1, 3, 3, 5]
    res = can_partition(numbers)
    return res


can_partition_test()


# %% [markdown]
# 474. 一和零
# https://leetcode-cn.com/problems/ones-and-zeroes/

#%%
def find_max_form(strlist: list[str], m: int, n: int):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for str in strlist:
        ones = str.count("1")
        zeros = str.count("0")
        for _i in range(m, zeros - 1, -1):
            for _j in range(n, ones - 1, -1):
                dp[_i][_j] = max(dp[_i][_j], dp[_i - zeros][_j - ones] + 1)
    return dp[m][n]


#%%
def find_max_form_test():
    strlist, m, n = ["10", "0001", "111001", "1", "0"], 5, 3
    result = find_max_form(strlist, m, n)
    print(result)


find_max_form_test()

# %% [markdown]
# 322. 零钱兑换
# https://leetcode-cn.com/problems/coin-change/

#%%
def coin_change(coins: list[int], amount: int):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for _j in range(coin, amount + 1):
            dp[_j] = min(dp[_j], dp[_j - coin] + 1)
    return dp[amount] if dp[amount] < amount + 1 else -1


#%%
def coin_change_test():
    coins = [1, 2, 5]
    amount = 11
    result = coin_change(coins, amount)
    print(result)


coin_change_test()

# %%
