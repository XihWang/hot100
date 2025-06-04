import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def quick_select(nums, k):
            pivot = random.choice(nums)
            big, small, equal = [], [], []
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)

            if k <= len(big):  # 如果第k大的元素在big中
                return quick_select(big, k)
            elif k > len(big) + len(equal):  # 如果第k大的元素在small中
                return quick_select(small, k - len(big) - len(equal))
            else:  # 如果第k大的元素就是pivot
                return pivot

        return quick_select(nums, k)


# import heapq
#
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         maxheap = []
#         nums = [-i for i in nums]
#         for i in nums:
#             heapq.heappush(maxheap, i)
#         for _ in range(k-1):
#             heapq.heappop(maxheap)
#         return -maxheap[0]


# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         n = len(nums)
#         l = 0
#         r = n - 1
#         def partition(nums, l, r):
#             pivot = nums[l]
#             while l < r:
#                 while l < r and nums[r] <= pivot:
#                     r -= 1
#                 nums[l] = nums[r]
#                 while l < r and nums[l] >= pivot:
#                     l += 1
#                 nums[r] = nums[l]
#             nums[l] = pivot
#             return l
#         while True:
#             index = partition(nums, l, r)
#             if index == k - 1:
#                 return nums[index]
#             elif index < k - 1:
#                 l = index + 1
#             else:
#                 r = index - 1



