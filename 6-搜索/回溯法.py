# %% [markdown]
# 46. 全排列
# >https://leetcode-cn.com/problems/permutations/
# >给定一个无重复数字的整数数组，求其所有的排列方式。


def permute(nums):
    def back_track(_first):
        if _first == n:
            res.append(nums[:])
        for _i in range(_first, n):
            nums[_first], nums[_i] = nums[_i], nums[_first] # 交换
            back_track(_first + 1)
            nums[_first], nums[_i] = nums[_i], nums[_first] # 恢复nums

    n = len(nums)
    res = []
    back_track(0)
    return res

# %% 
def permute_test():
    nums = [1,2,3]
    res = permute(nums)
    print(res)
permute_test()