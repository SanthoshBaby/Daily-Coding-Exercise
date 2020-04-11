class Solution:
    def markIslandLand( grid: List[List[str]],i,j,islandName):
        notMarkedIslands=["0","1"]
        if i in [-1,len(grid)] or j in [-1,len(grid[0])]:
            return False
        if grid[i][j] in notMarkedIslands and grid[i][j] == "1":
            grid[i][j]=islandName
            Solution.markIslandLand(grid,i,j+1,islandName)# Right 
            Solution.markIslandLand(grid,i+1,j,islandName)# Down
            Solution.markIslandLand(grid,i-1,j,islandName)# Up
            Solution.markIslandLand(grid,i,j-1,islandName)# Left
    def numIslands(self, grid: List[List[str]]) -> int:
        islandNo=0
        notMarkedIslands=["0","1"]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in notMarkedIslands and grid[i][j] == "1":
                    islandNo=islandNo+1
                    Solution.markIslandLand(grid,i,j,islandNo)
        return islandNo
