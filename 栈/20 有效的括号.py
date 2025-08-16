# 题解
# class Solution(object):
#     def isValid(self, s):
#         dc = {'}': '{', ']': '[', ')': '('}
#         st = []
#         for i in s:
#             if st and i in dc:
#                 if st[-1] == dc[i]:
#                     st.pop()
#                 else:
#                     return False
#             else:
#                 st.append(i)
#         return not st


# 我的方法 个人觉得我的方法不错
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        # if len(s) % 2 == 1:
        #     return False
        dc = {'}': '{', ']': '[', ')': '('}
        for i in s:
            if st and i in dc:
                if st[-1] == dc[i]:
                        st.pop()
                        continue
            st.append(i)
        return not st

# class Solution(object):
# 这个方法思想是错误的 因为有[{}]这样的
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         n = len(s)
#         dc = {'(':')', '{':'}', '[':']'}
#         for i in range(0,n,2):
#             if dc[s[i]] != s[i + 1]:
#                 return False
#         return True
