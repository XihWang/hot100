class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ls = [0] * n
        for i in bookings:
            ls[i[0] - 1] += i[2]
            if i[1] < n:
                ls[i[1]] -= i[2]

        res = [0] * n
        res[0] = ls[0]
        for i in range(1,n):
            res[i] = res[i-1] + ls[i]
        return res

