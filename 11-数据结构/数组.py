# %% [markdown]
# 448. 找到所有数组中消失的数字
# >给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

#%%
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n = len(nums)
    dic = {}
    for _i in range(1, n + 1):
        dic[_i] = 0
    for _, val in enumerate(nums):
        dic[val] += 1

    return [k for k,v in dic.items() if v == 0]

#%%
def find_disappeared_numbers_test():
    nums = [4,3,2,7,8,2,3,1]
    res = find_disappeared_numbers(nums)
    print(res)
find_disappeared_numbers_test()
