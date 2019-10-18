"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""


class Solution:
    def rotate(self, nums, k: int) -> None:
        nums_length = len(nums)
        if nums_length == k:
            return
        while k > nums_length:
            k -= nums_length
        new_list = [None] * nums_length
        for index in range(nums_length):
            new_index = index + k
            if new_index > nums_length - 1:
                new_index -= nums_length
            new_list[new_index] = nums[index]
        for index in range(nums_length):
            nums[index] = new_list[index]
        return

"""
Runtime: O(n). faster than  93.90%
"""
if __name__ == "__main__":
    lol = Solution()
    test = [1,2,3,4,5,6,7]
    lol.rotate(test, 3)