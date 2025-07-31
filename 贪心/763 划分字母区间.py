# from typing import List
# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         res = [-1]
#         n = len(s)
#         last_occurrence = {}
#         max_occurrence = 0
#         for idx, char in enumerate(s):
#             last_occurrence[char] = idx
#         for idx, char in enumerate(s):
#             max_occurrence = max(max_occurrence, last_occurrence[char])
#             if idx == max_occurrence:
#                 res.append(idx)
#         return [res[i + 1] - res[i] for i in range(len(res)-1)]

from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        n = len(s)
        last_occurrence = {}
        start = 0
        end = 0
        for idx, char in enumerate(s):
            last_occurrence[char] = idx
        for idx, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if idx == end:
                res.append(end - start + 1)
                start = idx + 1
        return res







