# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         need = {}
#         right = left = 0
#         window = {}
#         valid = 0
#         start = 0
#         length = float('inf')
#         for i in s1:
#             need[i] = need.get(i,0)+1
#         while right < len(s2):
#             c = s2[right]
#             right += 1
#             if c in need:
#                 window[c] = window.get(c,0) + 1
#                 if window[c] == need[c]:
#                     valid += 1
#
#             while valid == len(need):
#                 if right - left < length:
#                     length = right - left
#                     start = left
#                 d = s2[left]
#                 left += 1
#                 if d in need:
#                     if window[d] == need[d]:
#                         valid -= 1
#                     window[d] -= 1
#         return length == len(s1)
#

import collections
class Solution:
    # 判断 s 中是否存在 t 的排列
    def checkInclusion(self, t: str, s: str) -> bool:
        need, window = collections.defaultdict(int), collections.defaultdict(int)
        for c in t:
            need[c] += 1

        left, right, valid = 0, 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while (right - left >= len(t)):
                # 在这里判断是否找到了合法的子串
                if valid == len(need):
                    return True
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        # 未找到符合条件的子串
        return False

print(Solution().checkInclusion('ac','aoc'))