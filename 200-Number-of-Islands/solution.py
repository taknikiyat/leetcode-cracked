# https://leetcode.com/problems/number-of-islands/
# O(rows * cols) time | O(rows * cols) space
class Solution(object):
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":  # found and island
                    count += 1
                    self.callDFS(grid, i, j)
        return count
    
    def callDFS(self, grid, i, j):
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0"):
            return  # break if out of bounds or not a piece of land
        grid[i][j] = "0"  # mark as seen
        self.callDFS(grid, i - 1, j)  # go up
        self.callDFS(grid, i + 1, j)  # go down
        self.callDFS(grid, i, j - 1)  # go left
        self.callDFS(grid, i, j + 1)  # go right
