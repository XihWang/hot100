# class Solution(object):
#     def topKFrequent(self, nums, k):
#         time_dict = defaultdict(int)
#         for num in nums:
#             time_dict[num] += 1
#         # 更改字典，key为出现次数，value为相应的数字的集合
#         index_dict = defaultdict(list)
#         for key in time_dict:
#             index_dict[time_dict[key]].append(key)
#         # 排序
#         key = list(index_dict.keys())
#         key.sort()
#         result = []
#         cnt = 0
#         # 获取前k项
#         while key and cnt != k:
#             result+=index_dict[key[-1]]
#             cnt += 1
#             key.pop()

#         return result[0: k]

import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return []

        # 统计每个元素的频率
        count = Counter(nums)
        minheap = []
        res = []
        for num, freq in count.items():
            heapq.heappush(minheap, (freq, num))  # 对不同的元组排序默认是按照第0个元素的大小进行排序的
            if len(minheap) > k:
                heapq.heappop(minheap)
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        # 使用堆找出前 K 个高频元素
        return res
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         if not nums or k <= 0:
#             return []

#         # 统计每个元素的频率
#         count = Counter(nums)

#         # 使用堆找出前 K 个高频元素
#         return heapq.nlargest(k, count.keys(), key=count.get)

# 时间复杂度：O(nlogk)
# 空间复杂度：O(n)
# import heapq
#
#
# class Solution:
#     def topKFrequent(self, nums, k):
#         # 要统计元素出现频率
#         map_ = {}  # nums[i]:对应出现的次数
#         for i in range(len(nums)):
#             map_[nums[i]] = map_.get(nums[i], 0) + 1
#
#         # 对频率排序
#         # 定义一个小顶堆，大小为k
#         pri_que = []  # 小顶堆
#
#         # 用固定大小为k的小顶堆，扫描所有频率的数值
#         for key, freq in map_.items():
#             heapq.heappush(pri_que, (freq, key))
#             if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
#                 heapq.heappop(pri_que)
#
#         # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
#         result = [0] * k
#         for i in range(k - 1, -1, -1):
#             result[i] = heapq.heappop(pri_que)[1]
#         return result