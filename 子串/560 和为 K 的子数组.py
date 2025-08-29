class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0]
        n = len(nums)
        ct = 0
        for i in range(n):
            num = presum[i] + nums[i]
            presum.append(num)
        ans = 0
        cnt = defaultdict(int)
        for sj in presum:
            ans += cnt[sj - k] # 任何索引默认输出0
            cnt[sj] += 1
        return ans

