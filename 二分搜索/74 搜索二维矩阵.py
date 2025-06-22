# 排除法
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        n = len(matrix)
        m = len(matrix[0])
        j = m - 1
        while i < n and j >= 0:
            if matrix[i][j] > target:
                j = j - 1
            elif matrix[i][j] < target:
                i = i + 1
            else:
                return True
        return False


# 二分查找
# from typing import List
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         n = len(matrix)
#         m = len(matrix[0])
#         left = 0
#         right = m * n - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             x = matrix[mid // m][mid % m]
#             if x < target:
#                 left = mid + 1
#             elif x > target:
#                 right = mid - 1
#             else:
#                 return True
#         return False
