"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        string_length = len(s)
        palindrome_no = 0
        dynamic_table = [[False for x in range(string_length)] for y in range(string_length)]
        for i in range(string_length):
            dynamic_table[i][i] = True
            palindrome_no += 1
        for i in range(0, string_length-1):
            if s[i] == s[i+1]:
                dynamic_table[i][i+1] = True
                palindrome_no += 1
        word_length = 3
        while word_length <= string_length:
            for i in range(0, string_length - word_length + 1):
                j = i + word_length - 1
                if s[i] == s[j] and dynamic_table[i+1][j-1]:
                    dynamic_table[i][j] = True
                    palindrome_no += 1
            word_length += 1
        return palindrome_no


"""
Runtime: O(n * n). Runs faster than plain brute force due to optimization through dynamic programming
"""
if __name__ == "__main__":
    lol = Solution()
    string = "aba"
    print(lol.countSubstrings(string))
