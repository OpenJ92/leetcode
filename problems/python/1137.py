class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i == 0:
                return 0
            elif i == 1:
                return 1
            elif i == 2:
                return 1

            if i not in memo:
                memo[i] = dp(i - 3) + dp(i - 2) + dp(i - 1)

            return memo[i]
        return dp(n)

