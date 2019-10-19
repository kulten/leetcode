"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m = m - 1
        n = n - 1
        current_postion = m + n + 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[current_postion] = nums1[m]
                nums1[m] = 0
                current_postion -= 1
                m -= 1
            else:
                nums1[current_postion] = nums2[n]
                nums2[n] = 0
                current_postion -= 1
                n -= 1
        while m >= 0:
            nums1[current_postion] = nums1[m]
            current_postion -= 1
            m -= 1
        while n >= 0:
            nums1[current_postion] = nums2[n]
            current_postion -= 1
            n -= 1


"""
Runtime: O(m+n) where m and n are the length of the two arrays.
faster than 98%
"""
if __name__ == "__main__":
    list1 = [2,2,3,4,8,0,0,0, 0]
    list2 = [1,5,6,10]
    m = 5
    n = 4
    lol = Solution()
    lol.merge(list1, m, list2, n)
