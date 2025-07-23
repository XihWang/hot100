# 哈希表的方法 时间空间都是o(n)
# from typing import List
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         res = 1
#         nums = set(nums)
#         while res in nums:
#             res += 1
#         return res

from typing import List
class Solution:
    # 索引0放1 索引1放2
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                s = nums[i] - 1 # 注意这里一定要弄一个变量进行存储
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]是错的！！
                # 但nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] 是对的
                # why?
                # 先右边计算出一个元组 然后先赋值左边第一个，如果左边第一个是num[i]，他在左边第二个nums[nums[i] - 1]中还是出现了，这样会逻辑就混乱掉了 会无限循环（因为我的想法是右边的nums[i]）但实际上索引中的nums【i】是左边第一个 所以是错的！
                nums[s], nums[i] = nums[i], nums[s]

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1



# from typing import List


# class Solution:

#     # 3 应该放在索引为 2 的地方
#     # 4 应该放在索引为 3 的地方

#     def firstMissingPositive(self, nums: List[int]) -> int:
#         size = len(nums)
#         for i in range(size):
#             # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
#             while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
#                 self.__swap(nums, i, nums[i] - 1)

#         for i in range(size):
#             if i + 1 != nums[i]:
#                 return i + 1

#         return size + 1

#     def __swap(self, nums, index1, index2):
#         nums[index1], nums[index2] = nums[index2], nums[index1]

