"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ["(", "{", "["]
        closed_brackets = [")", "}", "]"]
        bracket_mapping = {"}": "{", "]": "[", ")": "("}
        stack = []
        if not s:
            return True
        if s[0] in closed_brackets:
            return False
        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif stack:
                last_char = stack.pop()
                mapping = bracket_mapping.get(char)
                if last_char != mapping:
                    return False
            else:
                return False
        if stack:
            return False
        return True


"""
Runtime: O(n). faster than 98%.
"""
if __name__ == "__main__":
    test = "["
    lol = Solution()
    print(lol.isValid(test))
