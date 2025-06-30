# class Solution(object):
#     def __init__(self):
#         self.res = []
#         self.trace = []
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         self.backtrace(nums, 0)
#         return self.res
#
#
#     def backtrace(self, nums, start):
#         self.res.append(list(self.trace))  # 注意这里必须要有list 不然就是保存了一个引用 如果self.trace变化了 所有的都会变化的 所以必须要有list函数形成一个新的引用
#         for i in range(start, len(nums)):
#             self.trace.append(nums[i])
#             self.backtrace(nums, i + 1)
#             self.trace.remove(nums[i])


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        trace = []
        res = []
        def backtrace(start):
            # 看做一个多叉树 不断的backtrace就是在不断的变深，而for循环是同一层内的
            res.append(trace[:])
            # if start == len(nums):  # 可以省略
            #     return
            for i in range(start, n):
                trace.append(nums[i])
                backtrace(i + 1)  # 因为子集是和顺序无关的 比如【1,2】和【2,1】一样的 所以是当前的i+1
                trace.pop()
        backtrace(0)
        return res
        # 过程 【】 1 12 123 13 2 23 3  不断变深再退回来换个方向继续深



