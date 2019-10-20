"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)
        if needle_len > haystack_len:
            return - 1
        if needle_len == 0:
            return 0
        auxiliary_arr = self.create_prefix_suffix_array(needle_len, needle)
        match_count = 0
        i = 0
        j = 0
        match_position = -1
        while i < haystack_len:
            if haystack[i] == needle[j]:
                match_count += 1
                if match_count == needle_len:
                    match_position = i - j
                    return match_position
                i += 1
                j += 1
            elif j != 0:
                j = auxiliary_arr[j-1]
                match_count = j
            else:
                i += 1
                match_count = 0
                match_position = -1
        return match_position

    @staticmethod
    def create_prefix_suffix_array(needle_len, needle):
        aux = [0] * needle_len
        i = 1
        j = 0
        while i < needle_len:
            if needle[i] == needle[j]:
                j += 1
                aux[i] = j
                i += 1
            elif j != 0:
                j = aux[j - 1]
            else:
                aux[i] = 0
                i += 1
        return aux

"""
Solved using Knuth–Morris–Pratt string-searching algorithm.
runtime: O(m+n) where m and n are the lengths of the needle and the haystack
"""
if __name__ == "__main__":
    lol = Solution()
    string = "mississippi"
    find = "issipi"
    print(lol.strStr(string, find))
