class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # left = right = 0
        # window = {}
        # length = 0
        # while right < len(s):
        #     c = s[right]
        #     right += 1

        #     while c in window:
        #         # length -= 1
        #         d = s[left]
        #         del window[d]
        #         left += 1
        #     if c not in window:
        #         window[c] = 1
        #         # length += 1
        #     length = max(length, right - left)
        # return length
        window = {}
        left, right = 0, 0
        # 记录结果
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            window[c] = window.get(c, 0) + 1
            # 判断左侧窗口是否要收缩
            while window.get(c) > 1:
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                window[d] -= 1
            # 在这里更新答案
            res = max(res, right - left)
        return res

