# from typing import List
# import copy
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         tmp = copy.deepcopy(matrix)
#         n = len(matrix)
#         for i in range(n):
#             for j in range(n):
#                 matrix[j][n - 1 - i] = tmp[i][j]


from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(n//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-i][j]
                matrix[n-1-i][j] = matrix[n-1-i][n-1-j]
                matrix[n - 1 - i][n - 1 - j] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = tmp
