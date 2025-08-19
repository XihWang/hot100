class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        st = []
        n = len(heights)
        left = [-1] * n
        for i in range(n):
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        st = [] # st.clear()
        right = [n] * n
        for i in range(n-1,-1,-1):
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        for h,l,r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1))
        return ans