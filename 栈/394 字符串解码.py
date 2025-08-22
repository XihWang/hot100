# class Solution(object):
#     def decodeString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         st = []
#         nums = []
#         num= ''
#         trace = ''
#         for i in range(len(s)):
#             if s[i] in '1234567890':
#                 num = num + s[i]
#                 if s[i+1] not in '1234567890':
#                     nums.append(num)
#                     num = ''
#             elif s[i] != ']':
#                 st.append(s[i])
#             else:
#                 while st:
#                     char = st.pop()
#                     if char == '[':
#                         break
#                     trace = char + trace
#                 trace = eval(nums.pop()) * trace
#                 st.append(trace)
#                 trace = ''
#         return ''.join(st)


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        num = 0
        st = []
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == '[':
                st.append([res, num])
                res, num = '', 0
            elif i == ']':
                result, number = st.pop()
                res = result + number * res
            else:
                res = res + i
        return res
