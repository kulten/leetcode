"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none)
deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while
"aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.



If there is no common subsequence, return 0.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        text1 = "0" + text1
        text2 = "0" + text2
        dynamic_table = [[0 for x in range(len(text1))] for y in range(len(text2))]
        for i in range(1, len(text2)):
            for j in range(1, len(text1)):
                if text1[j] == text2[i]:
                    dynamic_table[i][j] = dynamic_table[i-1][j-1] + 1
                else:
                    dynamic_table[i][j] = max(dynamic_table[i][j - 1], dynamic_table[i - 1][j])
        return dynamic_table[-1][-1]


"""
Runtime: O(n * m) where n amd m are the lengths of text1 and text2
"""
if __name__ == "__main__":
    t1 = "oxcpqrsvwf"
    t2 = "shmtulqrypy"
    lol = Solution()
    print(lol.longestCommonSubsequence(t1, t2))
