class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        max_len = max(map(len, wordDict))
        wordset = set(wordDict)
        @cache
        # 定义状态为 dp(i)，表示能否把前缀 s[:i]（表示 s[0] 到 s[i−1] 这段子串）划分成若干段，使得每段都在 wordDict 中。
        def dp(i):
            if i == 0:
                return True
            for j in range(i-1, max(i-max_len-1, -1), -1):  # 设 wordDict 中字符串的最长长度为 maxLen，枚举的上限不超过 maxLen，因为更长的子串必然不在 wordDict 中。
                if s[j:i] in wordset and dp(j):
                    return True
            return False
        return dp(n)


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         max_len = max(map(len, wordDict))  # 用于限制下面 j 的循环次数
#         words = set(wordDict)  # 便于快速判断 s[j:i] in words

#         n = len(s)
#         f = [True] + [False] * n
#         for i in range(1, n + 1):
#             for j in range(i - 1, max(i - max_len - 1, -1), -1):
#                 if f[j] and s[j:i] in words:
#                     f[i] = True
#                     break
#         return f[n]
