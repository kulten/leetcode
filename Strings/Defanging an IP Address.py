"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans_str = ""
        defang = "[.]"
        for index in range(0, len(address)):
            if address[index] == ".":
                ans_str += defang
            else:
                ans_str += address[index]
        return ans_str

"""
runtime: O(n). faster than 97%.
"""