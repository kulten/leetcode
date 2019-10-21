"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = dict()
        t_dict = dict()
        for character in s:
            exists = s_dict.get(character)
            if not exists:
                s_dict[character] = 1
            else:
                s_dict[character] += 1
        for character in t:
            exists = t_dict.get(character)
            if not exists:
                t_dict[character] = 1
            else:
                t_dict[character] += 1
        for character, count in s_dict.items():
            existing_value = t_dict.get(character, 0)
            if count != existing_value:
                return False
        return True


"""
runtime: O(n)
"""
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    lol = Solution()
    print(lol.isAnagram(s, t))