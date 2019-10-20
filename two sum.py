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
        value_cache = dict()
        for index in range(0, len(nums)):
            find = target - nums[index]
            if find in value_cache:
                return [index, value_cache[find]]
            else:
                value_cache[nums[index]] = index


"""
Runtime: O(n). Used a hashtable to reduce look up time fron O(n) to O(1)
"""
if __name__ == "__main__":
    lol = [3,2,4]
    target = 6
    s = Solution()
    print(s.twoSum(lol, target))