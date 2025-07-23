# from typing import List
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         n = len(intervals)
#         res = []
#         intervals.sort()
#         for i in range(n):
#             if res and res[-1][1] >= intervals[i][0]:
#                 res[-1][1] = max(res[-1][1], intervals[i][1])
#             else:
#                 res.append(intervals[i])
#         return res


from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大排序 里面key不需要 默认按照第0个排序的
        ans = []
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:  # 可以合并
                ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点最大值
            else:  # 不相交，无法合并
                ans.append(p)  # 新的合并区间
        return ans
