from typing import List
# 利用两个set存储横纵坐标 O(m + n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        ls = []
        m_set = set()
        n_set = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    m_set.add(i)
                    n_set.add(j)
        for i in range(m):
            for j in range(n):
                if i in m_set or j in n_set:
                    matrix[i][j] = 0


# 关键思想: 用matrix第一行和第一列记录该行该列是否有0,作为标志位
# O(1)
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         row = len(matrix)
#         col = len(matrix[0])
#         row0_flag = False
#         col0_flag = False
#         # 找第一行是否有0
#         for j in range(col):
#             if matrix[0][j] == 0:
#                 row0_flag = True
#                 break
#         # 第一列是否有0
#         for i in range(row):
#             if matrix[i][0] == 0:
#                 col0_flag = True
#                 break

#         # 把第一行或者第一列作为 标志位
#         for i in range(1, row):
#             for j in range(1, col):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = matrix[0][j] = 0
#         #print(matrix)
#         # 置0
#         for i in range(1, row):
#             for j in range(1, col):
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0

#         if row0_flag:
#             for j in range(col):
#                 matrix[0][j] = 0
#         if col0_flag:
#             for i in range(row):
#                 matrix[i][0] = 0

# 作者：powcai
# 链接：https://leetcode.cn/problems/set-matrix-zeroes/solutions/6594/o1kong-jian-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。