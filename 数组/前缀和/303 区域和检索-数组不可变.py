class NumArray(object):

    # def __init__(self, nums):
    #     """
    #     :type nums: List[int]
    #     """
    #     self.nums = nums
    #
    # def sumRange(self, left, right):
    #     """
    #     :type left: int
    #     :type right: int
    #     :rtype: int
    #     """
    #     ls = [0]
    #     for i in range(len(self.nums)):
    #         ls.append(ls[i] + self.nums[i])
    #     return ls[right + 1] - ls[left]

    # 上面的方法用了append 速度太慢了
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        self.s = s


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.s[right + 1] - self.s[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)