from typing import List

# 有一条河 0~n-1是河的两岸 从0到n-1
# [i,i+nums[i]]视作一座桥
# 在可以选的桥中 选择右端点最大的桥
# 走到这个桥的末端的时候，搭建以前记录的最长的桥
class Solution:
    def jump(self, nums: List[int]) -> int:
        ct = 0
        n = len(nums)
        farthest = 0
        next_right = 0
        # if n == 1:
        #     return 0
        for i in range(n - 1):  # i == n的时候就到了 不需要造桥了
            farthest = max(farthest, i + nums[i])
            if i == next_right:
                next_right = farthest
                ct += 1
        return ct

