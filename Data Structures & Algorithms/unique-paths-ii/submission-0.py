class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0]*cols for j in range(rows)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1]==1:
            return 0

        dp[0][0] = 1
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                if r==0 and c==0:
                    continue
                top = dp[r-1][c] if r>0 else 0
                left = dp[r][c-1] if c>0 else 0

                dp[r][c] = dp[r-1][c]+dp[r][c-1]

        return dp[rows-1][cols-1]
