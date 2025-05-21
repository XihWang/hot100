class Solution(object):
    def minDistance(self, W, N, wt, val):
        # 初始化一个二维数组dp，大小为(W+1) x (N+1)，所有元素初始值为0
        # dp[n][w]表示前n个物品在容量为w的背包中可以获得的最大价值  所以第0列和第0行自然为0，base case已经建立
        dp = [[0] * (N + 1) for i in range(W + 1)]

        # 外层循环遍历每个物品，从第1个物品到第N-1个物品（注意索引从0开始，所以是range(1, N)）
        for n in range(1, N):
            # 内层循环遍历每个背包容量，从1到W-1
            for w in range(1, W):
                # 如果当前物品的重量wt[n-1]大于当前背包容量w，则不能将该物品放入背包
                if w - wt[n - 1] < 0:
                    # 此时dp[n][w]等于不放入当前物品时的最大价值，即dp[n-1][w]
                    dp[n][w] = dp[n - 1][w]
                else:
                    # 否则，比较放入当前物品和不放入当前物品时的最大价值
                    # 放入当前物品时的最大价值为dp[n][w - wt[n - 1]] + val[n - 1]  # 注意wt和val都是从0开始 这里有个坐标偏移
                    # 不放入当前物品时的最大价值为dp[n-1][w]
                    dp[n][w] = max(
                        dp[n - 1][w],  # 不放入当前物品
                        dp[n][w - wt[n - 1]] + val[n - 1]  # 放入当前物品
                    )
        # 返回前N个物品在容量为W的背包中可以获得的最大价值
        return dp[N][W]
