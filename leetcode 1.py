"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        for first_index, _ in enumerate(nums):
            first_number = nums[first_index]
            if first_index + 1 < length:
                for second_index in range(first_index + 1, length):
                    second_number = nums[second_index]
                    two_sum = first_number + second_number
                    if two_sum == target:
                        return [first_index, second_index]


if __name__ == "__main__":
    lol = [3,2,4]
    target = 6
    s = Solution()
    print(s.twoSum(lol, target))