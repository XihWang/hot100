class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        st = []
        ans = 0
        for i in range(len(height)):
            while st and height[i] >= height[st[-1]]:
                bottom = height[st.pop()]
                if st:
                    left = height[st[-1]]
                    depth = min(left, height[i]) - bottom
                    ans += depth * (i - st[-1] - 1)
            st.append(i)
        return ans