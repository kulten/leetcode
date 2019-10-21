"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
"""


class Solution:
    def findCircleNum(self, M) -> int:
        circle = 0
        visited = [False] * len(M)
        total_people = len(M)
        for person in range(total_people):
            if visited[person]:
                continue
            circle += 1
            visited, matrix = self.dfs(M, visited, person)
        return circle

    def dfs(self, matrix, visited, person):
        if visited[person]:
            return visited, matrix
        visited[person] = True
        connections = matrix[person]
        for index, connection in enumerate(connections):
            if connection and not visited[index]:
                visited, matrix = self.dfs(matrix, visited, index)
        return visited, matrix

"""
Runtime O(n).
"""
if __name__ == "__main__":
    lol = Solution()
    friend_circle = [[1,0,0,1],
                     [0,1,1,0],
                     [0,1,1,1],
                     [1,0,1,1]]
    print(lol.findCircleNum(friend_circle))
