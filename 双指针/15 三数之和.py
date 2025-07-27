class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        output = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            if nums[R] + nums[R - 1] + nums[i] < 0:
                continue

            while L < R:
                if nums[L] + nums[i] + nums[R] > 0:
                    R = R - 1
                elif nums[L] + nums[i] + nums[R] < 0:
                    L = L + 1
                else:
                    output.append([nums[L], nums[i], nums[R]])
                    while nums[L] == nums[L + 1] and L < len(nums) - 2:
                        L += 1
                    while nums[R] == nums[R - 1] and R > -1:
                        R -= 1
                    L += 1
                    R -= 1
        return output


if __name__ == '__main__':
    # nums = [-1,0,1,2,-1,-4] # -4 -1 -1 0 1 2
    nums = [0,0,0]
    # nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(Solution().threeSum(nums))

