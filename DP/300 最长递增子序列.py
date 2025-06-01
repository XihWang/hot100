class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))  # 在他前面的比他小的数有多长 找出来
            return res + 1  # 选择自己还要增长一个
        return max(dfs(i) for i in range(n))


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         f = [0] * n
#         for i in range(n):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     f[i] = max(f[i], f[j])
#             f[i] = f[i] + 1
#         return max(f)
