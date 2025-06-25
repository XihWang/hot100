class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        for i in t:
            need[i] = need.get(i,0) + 1
        valid = 0
        window = {}
        left = right = 0
        length = float('inf')
        start = 0
        while right < len(s):
            val = s[right]
            window[val] = window.get(val, 0) + 1
            if val in need and window[val] == need[val]:
                valid += 1
            while valid == len(need):
                if right - left + 1 < length:
                    length = right - left + 1
                    start = left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:

                    valid -= 1
                left += 1
            right += 1

        return '' if length == float('inf') else s[start : start + length]



# 大佬的方法 更加合适  主体思想一致 就是写的更加优美
# class Solution(object):
#     def minWindow(self, s, t):
#         need, window = {}, {}
#         for c in t:
#             need[c] = need.get(c, 0) + 1
#
#         left = 0
#         right = 0
#         valid = 0
#         # 记录最小覆盖子串的起始索引及长度
#         start = 0
#         length = float('inf')
#         while right < len(s):
#             # c 是将移入窗口的字符
#             c = s[right]
#             # 扩大窗口
#             right += 1
#             # 进行窗口内数据的一系列更新
#             if c in need:
#                 window[c] = window.get(c, 0) + 1
#                 if window[c] == need[c]:
#                     valid += 1
#
#             # 判断左侧窗口是否要收缩
#             while valid == len(need):
#                 # 在这里更新最小覆盖子串
#                 if right - left < length:
#                     start = left
#                     length = right - left
#                 # d 是将移出窗口的字符
#                 d = s[left]
#                 # 缩小窗口
#                 left += 1
#                 # 进行窗口内数据的一系列更新
#                 if d in need:
#                     if window[d] == need[d]:
#                         valid -= 1
#                     window[d] -= 1
#
#         # 返回最小覆盖子串
#         return "" if length == float('inf') else s[start: start + length]