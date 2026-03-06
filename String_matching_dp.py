class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # def f(i,j):
        #     if j < 0:
        #         return 1
        #     if i < 0:
        #         return 0
        #     # two cases when we ecounter match
        #     # either we take the match or we dont take it 
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if s[i] == t[j]:
        #         pick = f(i-1, j-1)
        #         not_pick = f(i-1, j)
        #         dp[i][j] = pick + not_pick
        #         return dp[i][j]
        #     # the other case is when there isn't a match so we find more in s
        #     dp[i][j] = f(i-1,j)
        #     return dp[i][j]
        #     # these will be the only cases
    
        n = len(s)
        m = len(t)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        for j in range(m+1):
            dp[0][j] = 0
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    pick = dp[i-1][j-1]
                    not_pick = dp[i-1][j]
                    dp[i][j] = pick + not_pick
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]
