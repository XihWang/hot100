# 直接sort 不推荐
# from typing import List
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums1.extend(nums2)
#         nums1.sort()
#         n = len(nums1)
#         if n % 2:
#             return nums1[n // 2]
#         else:
#             return (nums1[n // 2] + nums1[n // 2 - 1]) / 2

# 没有二分
# from typing import List
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

#         if len(nums1) > len(nums2):
#             nums1, nums2 = nums2, nums1
#         m = len(nums1)
#         n = len(nums2)
#         nums1 = [-inf] + nums1 + [inf]
#         nums2 = [-inf] + nums2 + [inf]
#         i = 0
#         j = (m + n + 1) // 2
#         while True:
#             if nums1[i] <= nums2[j + 1] and nums1[i + 1] > nums2[j]:
#                 max1 = max(nums1[i], nums2[j])
#                 min2 = min(nums1[i + 1], nums2[j + 1])
#                 return max1 if (m+n)%2 else (min2 + max1) / 2
#             i += 1
#             j -= 1

# 有二分
# class Solution:
#     def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
#         if len(a) > len(b):
#             a, b = b, a

#         m, n = len(a), len(b)
#         a = [-inf] + a + [inf]
#         b = [-inf] + b + [inf]

#         # 循环不变量：a[left] <= b[j+1]
#         # 循环不变量：a[right] > b[j+1]
#         left, right = 1, m
#         while left <= right:  # 闭区间 [left, right] 不为空
#             i = (left + right) // 2
#             j = (m + n + 1) // 2 - i
#             if a[i] <= b[j + 1]:  # <= <都可以
#                 left = i + 1  # 缩小二分区间为 (i, right)
#             else:
#                 right = i - 1  # 缩小二分区间为 (left, i)

#         # 此时 left 等于 right+1
#         # a[right] <= b[j+1] 且 a[left] > b[j'+1] = b[j]，所以答案是 i=right
#         i = right
#         j = (m + n + 1) // 2 - i
#         max1 = max(a[i], b[j])
#         min2 = min(a[i + 1], b[j + 1])
#         return max1 if (m + n) % 2 else (max1 + min2) / 2

# # 作者：灵茶山艾府
# # 链接：https://leetcode.cn/problems/median-of-two-sorted-arrays/solutions/2950686/tu-jie-xun-xu-jian-jin-cong-shuang-zhi-z-p2gd/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 去掉inf二分
# 前面时间复杂度都是O(m+n)
# 这个是O(logmin(m,n))
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a

        m, n = len(a), len(b)
        # 循环不变量：a[left] <= b[j+1]
        # 循环不变量：a[right] > b[j+1]
        left, right = 0, m - 1
        while left <= right:  # 开区间 (left, right) 不为空
            i = (left + right) // 2
            j = (m + n - 3) // 2 - i
            if a[i] <= b[j + 1]:
                left = i + 1  # 缩小二分区间为 (i, right)
            else:
                right = i - 1  # 缩小二分区间为 (left, i)

        # 此时 left 等于 right+1
        # a[left] <= b[j+1] 且 a[right] > b[j'+1] = b[j]，所以答案是 i=left
        i = right
        j = (m + n - 3) // 2 - i
        ai = a[i] if i >= 0 else -inf
        bj = b[j] if j >= 0 else -inf
        ai1 = a[i + 1] if i + 1 < m else inf
        bj1 = b[j + 1] if j + 1 < n else inf
        max1 = max(ai, bj)
        min2 = min(ai1, bj1)
        return max1 if (m + n) % 2 else (max1 + min2) / 2

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/median-of-two-sorted-arrays/solutions/2950686/tu-jie-xun-xu-jian-jin-cong-shuang-zhi-z-p2gd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
