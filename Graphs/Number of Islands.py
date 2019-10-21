"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
"""


class Solution:
    def numIslands(self, M) -> int:
        if not M:
            return 0
        islands = 0
        height = len(M) - 1
        width = len(M[0]) - 1
        for i, row in enumerate(M):
            for j, column in enumerate(row):
                if column == "1":
                    islands += 1
                    self.dfs(M, i, j, height, width)
        return islands

    def dfs(self, matrix, i, j, height, width):
        if i < 0 or i > height or j < 0 or j > width or matrix[i][j] == "0":
            return
        matrix[i][j] = "0"
        self.dfs(matrix, i, j + 1, height, width)  # Go right
        self.dfs(matrix, i + 1, j, height, width)  # Go down
        self.dfs(matrix, i, j - 1, height, width)  # Go left
        self.dfs(matrix, i - 1, j, height, width)  # Go up
        return


"""
Runtime: O(n*n).
"""
if __name__ == "__main__":
    lol = Solution()
    input_list = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(lol.numIslands(input_list))
