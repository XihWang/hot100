# 逆序的单调栈， 进来的比原来栈内的大，就把比这个数小的出栈。

# class Solution(object):
#     def dailyTemperatures(self, temperatures):
#         """
#         :type temperatures: List[int]
#         :rtype: List[int]
#         """
#         n = len(temperatures)
#         st = []
#         ans = [0] * n
#         for i in range(n-1, -1, -1):
#             while st and temperatures[i] >= temperatures[st[-1]]:
#                 st.pop()
#             if st:
#                 ans[i] = st[-1] - i
#             st.append(i)
#         return ans

# 正序的单调栈
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        st = []
        ans = [0] * n
        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)
        return ans



