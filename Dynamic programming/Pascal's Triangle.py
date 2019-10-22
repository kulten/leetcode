"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, num_rows):
        triangle = [[None for j in range(i+1)] for i in range(num_rows)]
        for i in range(0, num_rows):
            for j in range(0, i + 1):
                if i - 1 < 0 or j - 1 < 0 or j == i:
                    triangle[i][j] = 1
                else:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle


"""
Runtime: O(n*n)
"""
if __name__ == "__main__":
    lol = Solution()
    print(lol.generate(5))
