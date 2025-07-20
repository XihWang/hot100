class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        ls = [0] * 1001
        for i in trips:
            ls[i[1]] += i[0]
            ls[i[2]] -= i[0]
            # ls[i[2]+1] -= i[0]
        res = [0] * 1001
        res[0] = ls[0]
        for i in range(1,1001):
            res[i] = res[i - 1] + ls[i]
        for i in res:
            if i > capacity:
                return False
        return True

