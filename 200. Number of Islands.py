class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    Count += 1
                    self.sink(grid, row, col)
        
        return Count
    
    def sink(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        self.sink(grid, row + 1, col)
        self.sink(grid, row - 1, col)
        self.sink(grid, row, col + 1)
        self.sink(grid, row, col - 1)
            
    
