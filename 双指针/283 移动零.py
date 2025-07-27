# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         if 0 in nums:
#             count = nums.count(0)
#             for i in range(count):
#                 idx = nums.index(0)
#                 nums.append(nums.pop(idx))
#
#         return nums


class Solution:
    # 用right指针遍历 把left留在0的地方
    # 不等于0就往前换
    # 左指针左边均为非零数；
    #
    # 右指针左边直到左指针处均为零。
    def moveZeroes(self, nums) :
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        return nums





if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print(Solution().moveZeroes(nums))
