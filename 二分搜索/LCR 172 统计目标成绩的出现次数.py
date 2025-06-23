class Solution(object):
    def countTarget(self, scores, target):
        """
        :type scores: List[int]
        :type target: int
        :rtype: int
        """
        # 速度太慢
        # count = 0
        # while target in scores:
        #     count += 1
        #     scores.remove(target)
        # return count

        left = 0
        right = len(scores) - 1
        count = 0
        if len(scores) == 0:
            return 0
        if target < scores[left] or target > scores[right]:
            return 0
        while left <= right:
            mid = left + (right - left) // 2
            if scores[mid] == target:
                right = mid - 1
            elif scores[mid] < target:
                left = mid + 1
            elif scores[mid] > target:
                right = mid - 1
        while left < len(scores) and scores[left] == target: # 注意这里的两个判断必须left < len(scores) 在前  否则就会报越界错误
            count += 1
            left += 1
        return count
