"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, nums) -> int:
        dynamic_table = [0] * len(nums)
        dynamic_table[0] = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            potential_max = nums[i]
            current_max = dynamic_table[i - 1] + potential_max
            dynamic_table[i] = max(current_max, potential_max)
            max_sum = max(max_sum, dynamic_table[i])
        return max_sum

"""
Runtime: O(n). Dynamic programming
"""
if __name__ == "__main__":
    lol = Solution()
    list1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(lol.maxSubArray(list1))
