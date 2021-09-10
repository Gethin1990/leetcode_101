# %% [markdown]
# 70. 爬楼梯
# >假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# step:
# 1. def dp
# 2. def dp init 最小就
# 3. dp 推导式

# %%
class climb_stairs_solution:
    def climb_stairs_1(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def climb_stairs_2(self, n: int) -> int:
        a = b = 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def climb_stairs_test(self):
        r1 = self.climb_stairs_1(7)
        print(r1)
        r2 = self.climb_stairs_2(7)
        print(r2)


# %%
s1 = climb_stairs_solution()
s1.climb_stairs_test()

# %% [markdown]
# 198. 打家劫舍
# >你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# >给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

# %%
class rob_solution:
    def rob_1(self, nums) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N == 1:
            return nums[0]
        dp = [0] * (N)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[N - 1]

    def rob_2(self, nums) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        return second

    def rob_test(self):
        nums = [2, 7, 9, 3, 1]
        r1 = self.rob_1(nums)
        print(r1)
        r2 = self.rob_2(nums)
        print(r2)


# %%
s2 = rob_solution()
s2.rob_test()

# %% [markdown]
# 413. 等差数列划分
# >给定一个数组，求这个数组中连续且等差的子数组一共有多少个。
class number_of_arithmetic_slices_solution:
    def number_of_arithmetic_slices(self, nums):
        N = len(nums)
        if N < 3:
            return 0
        dp = [0] * N
        for i in range(2, N):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)

    def number_of_arithmetic_slices_test(self):
        nums = [1, 2, 3, 4]
        result = self.number_of_arithmetic_slices(nums)
        print(result)


# %%


s3 = number_of_arithmetic_slices_solution()
s3.number_of_arithmetic_slices_test()
# %%
