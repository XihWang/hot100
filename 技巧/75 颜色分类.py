# from typing import List
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         def partition(nums, low, high):
#
#             p = nums[low]
#             i = low
#             for j in range(low + 1, high):
#                 if p > nums[j]:
#                     i += 1
#                     nums[j], nums[i] = nums[i], nums[j]
#             nums[i], nums[low] = nums[low], nums[i]
#             return i
#         def quicksort(nums, low, high):
#             if low >= high:
#                 return
#
#             idx = partition(nums, low, high)
#             quicksort(nums, low, idx)
#             quicksort(nums, idx + 1, high)
#
#         n = len(nums)
#         quicksort(nums, 0, n)


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = 0
        two = n - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                # 注意two这里的i不能-1 因为后面换到前面来的还没有判断过 所以i不能动要判断
                # 但是==0的时候 前面换到i的 已经判断过了 所以i能＋1
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1





