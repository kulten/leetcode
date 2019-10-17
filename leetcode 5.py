"""
Problem statement:
    5. Longest Palindromic Substring
        Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

        Example 1:
        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.

        Example 2:
        Input: "cbbd"
        Output: "bb"
    Solution: Solved by using dynamic programming

"""


class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        palindrome = ""
        palindrome_length = 0
        str_len = len(s)
        dynamic_table = [[False for x in range(len(s))] for y in range(len(s))]
        for i in range(0, str_len):
            dynamic_table[i][i] = True
            palindrome = s[i]
        if str_len <= 1:
            return palindrome
        for i in range(0, str_len-1):
            if s[i] == s[i+1]:
                dynamic_table[i][i+1] = True
                palindrome = s[i:i+2]
        if str_len == 2:
            return palindrome
        word_length = 3
        while word_length <= str_len:
            i = 0
            while i + word_length - 1 < str_len:
                j = i + word_length - 1
                if s[i] == s[j] and dynamic_table[i+1][j-1]:
                    dynamic_table[i][j] = True
                    if word_length > palindrome_length:
                        palindrome = s[i: j+1]
                i += 1
            word_length += 1
        return palindrome


if __name__ == "__main__":
    string = "asloaaoldf"
    lol = Solution()
    print(lol.longestPalindrome(string))