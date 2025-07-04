# from typing import List
# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         ct = Counter(nums)
#         ls = list(ct.items()).sort(key = lambda p:p[1])
#         return ls[-1][0]

# from typing import List
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums) // 2
#         nums.sort()
#         return nums[n]


from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        for i in nums:
            if vote == 0:
                x = i
            if i == x:
                vote += 1
            else:
                vote -= 1
        return x


