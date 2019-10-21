"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_char = -1
        if not s:
            return unique_char
        alphabet_map = dict()
        for character in s:
            if character in alphabet_map:
                alphabet_map[character] += 1
            else:
                alphabet_map[character] = 1
        for index, character in enumerate(s):
            occurance = alphabet_map.get(character)
            if occurance == 1:
                unique_char = index
                return unique_char
        return unique_char


"""
Runtime: O(n)
"""
if __name__ == "__main__":
    lol = Solution()
    s = "cc"
    print(lol.firstUniqChar(s))
