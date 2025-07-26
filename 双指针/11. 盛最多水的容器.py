class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 方法1 暴力（时间溢出）
        # area = 0
        #
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         length = j-i
        #         htl = height[i]
        #         htr = height[j]
        #         ht = htl if htl < htr else htr
        #         if length * ht > area:
        #             area = length * ht
        # return  area


        area = 0
        L = 0
        R = len(height)-1
        while L < R:
            htl = height[L]
            htr = height[R]
            ht = htl if htl < htr else htr
            length = R - L
            if ht * length > area:
                area = ht * length
            if height[L] > height[R]:
                R = R - 1
            else:
                L = L + 1

        return area


if __name__ == "__main__":
    nums = [1,8,6,222,5,43,8,3,7]
    print(Solution().maxArea(nums))