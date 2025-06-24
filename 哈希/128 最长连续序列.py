from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        需要用O（n）的复杂度
        """
        st = set(nums)
        ans = 0 # 注意这里不是1  否则[]列表会返回1
        for x in st:
            if x-1 in st:
                continue
            y = x+1
            while y in st:
                y += 1
            ans = max(y-x,ans)
        return ans





if __name__ == '__main__':
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(Solution().longestConsecutive(nums))