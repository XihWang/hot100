class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left = right = 0
        res = []
        need = {}
        window = {}
        valid = 0
        for i in p:
            need[i] = need.get(i, 0) + 1
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while right - left >= len(p):  # 注意这里有一个=号
                # 确保每次刚好长度到的时候 就进行判别
                # 可以改成right - left == len(p)
                if valid == len(need):
                    res.append(left)
                d = s[left]
                if d in need:
                # 这里不对 不然刚好本来就小于 就会继续减少valid
                    # window[d] -= 1
                    # if window[d] < need[d]:
                    #     valid -= 1
                # 它确保了只有当窗口中某个字符的数量从刚好满足需求变为不满足需求时，才会减少
                # valid。
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                left += 1

        return res

