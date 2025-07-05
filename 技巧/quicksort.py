# 方法一单方向遍历
def partition(nums, low, high):
    p = nums[low]
    i = low
    for j in range(low + 1, high):
        if p >= nums[j]:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[i], nums[low] = nums[low], nums[i]
    # 注意哨兵不能放在替换中 而要在最后一步进行替换
    # p >= nums[j]:从小到大  p <= nums[j]就是从大到小
    return i


def quicksort(nums, low, high):
    if low >= high:
        return

    idx = partition(nums, low, high)
    # 个人喜欢左闭右开
    # for j in range(low + 1, high+1):
    # 就是左闭左闭
    quicksort(nums, low, idx)
    quicksort(nums, idx + 1, high)
#
#
# nums = [3, 6, 8, 10, 1, 2, 1]
# n = len(nums)
# quicksort(nums, 0, n)  # 修改此处
# print(nums)

# 列表推导式
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]  # 选择中间元素为基准
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#
# # 调用示例
# sorted_nums = quick_sort([3, 1, 4, 1, 5, 9, 2, 6])
# print(sorted_nums)  # 输出：[1, 1, 2, 3, 4, 5, 6, 9]


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         l = 0
#         r = n - 1
#         while True:
#             idx = self.partition(nums, l, r)
#             if idx == k - 1:
#                 return nums[idx]
#             elif idx < k - 1:
#                 l = idx + 1
#             else:
#                 r = idx - 1
#
#
#     #----左右挖坑互填
#     def partition(self, nums: List[int], l: int, r: int) -> int:
#         pivot = nums[l]
#         while l < r:
#             while l < r and nums[r] <= pivot:
#                 r -= 1
#             nums[l] = nums[r]
#             while l < r and nums[l] >= pivot:
#                 l += 1
#             nums[r] = nums[l]
#
#         nums[l] = pivot
#         return l




# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         l = 0
#         r = n - 1
#         while True:
#             idx = self.partition(nums, l, r)
#             if idx == k - 1:
#                 return nums[idx]
#             elif idx < k - 1:
#                 l = idx + 1
#             else:
#                 r = idx - 1


    #----左右交换
#     def partition(self, nums: List[int], l: int, r: int) -> int:
#         pivot = nums[l]
#         begin = l
#         while l < r:
#             while l < r and nums[r] <= pivot:
#                 r -= 1
#             while l < r and nums[l] >= pivot:
#                 l += 1
#             if l < r:
#                 nums[l], nums[r] = nums[r], nums[l]
#         nums[begin], nums[l] = nums[l], nums[begin]
#         return l








