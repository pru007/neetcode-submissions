class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1,2]
        i=3
        while i<=n:
            temp = dp[0]
            dp[0] = dp[1]
            dp[1] = dp[1] + temp
            i = i + 1
        return dp[1]
        # return climbStairs(n-1) + climbStairs(n-2)