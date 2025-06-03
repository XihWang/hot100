class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(memo, n):
            if n == 0 or n == 1:
                return n
            if memo[n] != 0:
                return memo[n]
            memo[n] = helper(memo, n-1) + helper(memo, n-2)
            return memo[n]
        memo = [0] * (n + 1)
        return helper(memo, n)

