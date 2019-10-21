"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""


class Solution:
    def reverseString(self, s) -> None:
        if not s:
            return

        def reverse(string, first_index, last_index):
            if first_index == last_index or last_index < first_index:
                return
            string[first_index], string[last_index] = string[last_index], string[first_index]
            reverse(string, first_index + 1, last_index - 1)
            return

        reverse(s, 0, len(s) - 1)
        return

"""
Runtime: O(n/2)
"""