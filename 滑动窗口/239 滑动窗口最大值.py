# 暴力O（n^2） 超时
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         left = 0
#         right = k
#         res = []
#         n = len(nums)
#         while right <= n:
#             ans = max(nums[left: right])
#             res.append(ans)
#             left += 1
#             right += 1
#         return res


# 队列 O(n)
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        res = []
        for i in range(n):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i - q[0] + 1 > k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res




