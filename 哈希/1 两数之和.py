# 1 两数之和
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums1 = sorted(nums)
        L = 0
        R = len(nums1) - 1
        while L< R:
            s = nums1[L] + nums1[R]
            if s == target:
                break
            elif s > target:
                R -= 1
            else:
                L+=1
        L = nums.index(nums1[L])
        nums[L] = float('inf')
        R = nums.index(nums1[R])
        if L> R:
            R,L = L,R
        output = [L,R]
        return output



# 灵神的方法
# class Solution:
#     def twoSum(self, nums, target):
#         idx = {}  # 创建一个空哈希表（字典）
#         for j, x in enumerate(nums):  # x=nums[j]
#             if target - x in idx:  # 在左边找 nums[i]，满足 nums[i]+x=target
#                 return [idx[target - x], j]  # 返回两个数的下标
#             idx[x] = j  # 保存 nums[j] 和 j


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))


