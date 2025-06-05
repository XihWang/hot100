# 时间太长了
# class MedianFinder(object):
#
#     def __init__(self):
#         self.ls = []
#
#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: None
#         """
#         self.ls.append(num)
#
#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         n = len(self.ls)
#         self.ls.sort()
#         if n == 0:
#             return
#         elif n % 2 == 1:
#             return self.ls[n // 2]
#         elif n % 2 == 0:
#             return (self.ls[n // 2] + self.ls[(n // 2) - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# import heapq
# class MedianFinder(object):
#
#     def __init__(self):
#         self.left = [] # 最大堆
#         self.right = [] # 最小堆
#         # 那么每次就是对左边的最大值和右边的最小值进行处理
#         # 规定左边可以比右边多一个
#
#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: None
#         """
#         if len(self.left) == len(self.right):
#             heapq.heappush(self.right, num)
#             heapq.heappush(self.left, -heapq.heappop(self.right))
#         else:
#             heapq.heappush(self.left, -num)
#             heapq.heappush(self.right, -heapq.heappop(self.left))
#
#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         if len(self.left) == len(self.right):
#             numleft = - heapq.heappop(self.left)
#             numright = heapq.heappop(self.right)
#             heapq.heappush(self.left, -numleft)
#             heapq.heappush(self.right, numright)
#             return (numleft + numright) / 2
#         else:
#             numleft = - heapq.heappop(self.left)
#             heapq.heappush(self.left, -numleft)
#             return numleft

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

from heapq import heappush,heappushpop
class MedianFinder:
    def __init__(self):
        self.left = []  # 入堆的元素取相反数，变成最大堆
        self.right = []  # 最小堆

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heappush(self.left, -heappushpop(self.right, num))
        else:
            heappush(self.right, -heappushpop(self.left, -num))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (self.right[0] - self.left[0]) / 2
