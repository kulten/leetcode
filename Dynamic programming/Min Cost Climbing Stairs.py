"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps.
You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0,
or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
"""


class Solution:
    def minCostClimbingStairs(self, cost):
        stair1 = cost[0]
        stair2 = cost[1]
        for i in range(2, len(cost)):
            current_stair = cost[i] + min(stair1, stair2)
            stair1 = stair2
            stair2 = current_stair
        return min(stair1, stair2)


"""
Runtime: O(n)
"""
if __name__ == "__main__":
    lol = Solution()
    cost = [0,1,1,1]
    cost1 =  [0,1,1,0]
    cost3 = [0,0,0,1]
    print(lol.minCostClimbingStairs(cost1))
