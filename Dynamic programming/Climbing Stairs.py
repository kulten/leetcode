"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""


class Solution:
    def climbStairs(self, n: int):
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for stair in range(3, n+1):
            dp[stair] = dp[stair-1] + dp[stair-2]
        return dp[n]

"""
Runtime: O(n)
"""
if __name__ == "__main__":
    lol = Solution()
    print(lol.climbStairs(35))

