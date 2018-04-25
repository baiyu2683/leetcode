"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""

def twoSum(nums, target):
    result = []
    len_nums = len(nums)
    for i in range(len_nums):
        f = nums[i]
        for j in range(i + 1, len_nums):
            s = nums[j]
            print(i, j)
            if f + s == target:
                result.append(f)
                result.append(s)
                return result

nums = [1,2,3,4,7]
target = 6
result = twoSum(nums, target)
print(result)

